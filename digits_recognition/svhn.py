from torch.utils.data import Dataset
from os import path
import pickle
from skimage import io
from digits_struct_reader import DigitsStructReader
import numpy as np

MAT_FILE = 'digitStruct.mat'
PICKLE_FILE = 'digitStruct.pickle'

N_DIGITS = 13
N_LABELS = 7
GO = 10
STOP = 11
PAD = 12

VAL_INITIAL_INDEX = 27000

class SVHN(Dataset):

    _root_dir = ''
    _data = None
    _transform = None

    def __init__(self, root_dir, split, transform=None):
        self._transform = transform
        directory = self._get_directory(split)
        self._root_dir = path.join(root_dir, directory)
        self._load_data()
        self._slice_split_indices(split)

    def _get_directory(self, split):
        if split in ['train', 'val', 'train_val']:
            return 'train'
        elif split == 'test':
            return 'test'

    def _load_data(self):
        pickle_file_path = path.join(self._root_dir, PICKLE_FILE)
        print('Loading data from {}.'.format(self._root_dir))
        if path.exists(pickle_file_path):
            print('Loading data with pickle.')
            self._load_pickle_data(pickle_file_path)
        else:
            print('Loading data from digitsStruct.mat.')
            mat_file_path = path.join(self._root_dir, MAT_FILE)
            self._load_mat_data(mat_file_path)
            self._dump_pickle_data(pickle_file_path)

    def _load_pickle_data(self, pickle_file_path):
        with open(pickle_file_path, 'rb') as file:
            self._data = pickle.load(file)

    def _load_mat_data(self, mat_file_path):
        self._data = None
        reader = DigitsStructReader(mat_file_path)
        self._data = reader.read(self._root_dir)

    def _dump_pickle_data(self, pickle_file_path):
        with open(pickle_file_path, 'wb') as file:
            pickle.dump(self._data, file, pickle.HIGHEST_PROTOCOL)

    def _slice_split_indices(self, split):
        if split == 'train':
            for key in self._data.keys():
                self._data[key] = self._data[key][:VAL_INITIAL_INDEX]
        elif split == 'val':
            for key in self._data.keys():
                self._data[key] = self._data[key][VAL_INITIAL_INDEX:]

    def __len__(self):
        return len(self._data['paths'])

    def __getitem__(self, index):
        bbox = self._get_bounding_box(index)
        image_path = self._data['paths'][index]
        image = io.imread(image_path)
        image = self._crop_image(image, bbox)
        image = self._pad_image(image, bbox)

        labels = self._data['label'][index]
        labels = self._format_labels(labels)
        input_labels = self._prepare_input_labels(labels)
        output_labels = self._prepare_output_labels(labels)

        if self._transform:
            image = self._transform(image)

        return (image, input_labels, output_labels)

    def _get_bounding_box(self, i):
        data = self._data

        top = np.min(data['top'][i])
        bottoms = [sum(x) for x in zip(data['top'][i], data['height'][i])]
        height = np.max(bottoms) - top

        left = np.min(data['left'][i])
        rights = [sum(x) for x in zip(data['left'][i], data['width'][i])]
        width = np.max(rights) - left

        center = (float(top + top + height) / 2.0,
                  float(left + left + width) / 2.0)
        width = height = np.max([width, height])

        left = int(center[1] - (width / 2.0))
        top = int(center[0] - (height / 2.0))

        return (left, top, width, height)

    def _crop_image(self, image, bbox):
        (left, top, width, height) = bbox
        left = np.max([left, 0])
        top = np.max([top, 0])
        right = np.min([left + width, image.shape[1]])
        bottom = np.min([top + height, image.shape[0]])

        image = image[top:bottom, left:right]

        return image

    def _pad_image(self, image, bbox):
        (width, height) = bbox[2:]
        padded = np.zeros((height, width, 3), dtype=image.dtype)
        padded[:image.shape[0], :image.shape[1], :] = image
        return padded

    def _format_labels(self, labels):
        # Number 0 has label number 10
        return [label % 10 for label in labels]

    def _prepare_input_labels(self, labels):
        input_labels = [GO]
        for label in labels:
            input_labels.append(label)

        self._pad_labels(input_labels)
        return input_labels

    def _prepare_output_labels(self, labels):
        output_labels = []
        for label in labels:
            output_labels.append(label)
        output_labels.append(STOP)
        self._pad_labels(output_labels)
        return output_labels

    def _pad_labels(self, labels):
        while len(labels) < N_LABELS:
            labels.append(PAD)
