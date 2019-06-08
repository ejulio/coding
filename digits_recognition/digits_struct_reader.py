# some help from
# https://stackoverflow.com/questions/33509163/how-to-read-mat-v7-3-files-in-python
import h5py
from os import path
import logging


class DigitsStructReader(object):

    _data_file_path = None
    _data = None
    _data_file = None

    def __init__(self, data_file_path):
        self._data_file_path = data_file_path

    def _get_attrs(self, name, obj):
        vals = []
        if obj.shape[0] == 1:
            vals.append(int(obj[0][0]))
        else:
            for k in range(obj.shape[0]):
                vals.append(int(self._data_file[obj[k][0]][0][0]))

        self._data[name].append(vals)

    def read(self, images_base_path):
        self._data_file = h5py.File(self._data_file_path)
        self._init_data()
        self._read_image_names(images_base_path)
        self._read_labels_and_bounding_boxes()
        return self._data

    def _init_data(self):
        self._data = {}
        self._data['paths'] = []
        self._data['label'] = []
        self._data['height'] = []
        self._data['left'] = []
        self._data['top'] = []
        self._data['width'] = []

    def _read_image_names(self, images_base_path):
        logging.info('Reading images names.')
        column = self._data_file['digitStruct']['name']
        for item in column:
            image_name = map(chr, self._data_file[item[0]][:])
            image_path = path.join(images_base_path, ''.join(image_name))
            self._data['paths'].append(image_path)

    def _read_labels_and_bounding_boxes(self):
        logging.info('Reading images labels and bounding boxes.')
        column = self._data_file['digitStruct']['bbox']
        for item in column:
            self._data_file[item[0]].visititems(self._get_attrs)
