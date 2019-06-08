import svhn
import digits_model
import numpy as np
from skimage import io, exposure
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import optim, nn
from torch.autograd import Variable
from torch.optim import lr_scheduler
import torch
import collections

np.random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)

BATCH_SIZE = 128


def collate(batch):
    transposed = zip(*batch)
    (images, input_labels, output_labels) = list(transposed)
    images = torch.stack(images, 0)
    input_labels = torch.LongTensor(input_labels)
    output_labels = torch.LongTensor(output_labels)
    return (images, input_labels, output_labels)


composed = transforms.Compose([transforms.ToPILImage(),
                               transforms.Scale(100),
                               transforms.ToTensor(),
                               transforms.Normalize([0.485, 0.456, 0.406],
                                                    [0.229, 0.224, 0.225])])
train_dataset = svhn.SVHN('./svhn', split='train', transform=composed)
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE,
                              shuffle=True, num_workers=0,
                              collate_fn=collate)
n_iters = len(train_dataloader)

val_dataset = svhn.SVHN('./svhn', split='val', transform=composed)
val_dataloader = DataLoader(val_dataset, batch_size=1, num_workers=0,
                            collate_fn=collate)

test_dataset = svhn.SVHN('./svhn', split='test', transform=composed)
test_dataloader = DataLoader(test_dataset, batch_size=1,
                             shuffle=True, num_workers=0,
                             collate_fn=collate)

encoder = digits_model.Encoder()
encoder.cuda()

decoder = digits_model.Decoder(n_digits=svhn.N_DIGITS)
decoder.cuda()

parameters = list(encoder.parameters()) + list(decoder.parameters())
sgd = optim.SGD(parameters, lr=0.1, momentum=0.7, weight_decay=0.00005)
lr_decay_scheduler = lr_scheduler.StepLR(sgd, step_size=30, gamma=0.1)

nll = nn.NLLLoss(ignore_index=svhn.PAD)

for epoch in range(61):
    lr_decay_scheduler.step()
    print('Epoch {}, lr = {}'.format(epoch, sgd.param_groups[0]['lr']))
    decoder.train(True)
    encoder.train(True)
    losses = []
    for (i, batch) in enumerate(train_dataloader):
        (images, input_labels, output_labels) = batch
        images = Variable(images.cuda())
        input_labels = Variable(input_labels.cuda())
        output_labels = Variable(output_labels.cuda())

        sgd.zero_grad()
        batch_size = images.size()[0]
        decoder.reset_state(batch_size)
        images_embeddings = encoder(images)
        decoder.input_images(images_embeddings)
        predictions = decoder(input_labels)

        loss = nll(predictions, output_labels.view(svhn.N_LABELS * batch_size))
        loss.backward()
        sgd.step()

        losses.append(loss.data[0])
        running_loss = float(sum(losses)) / float(len(losses))
        print('Loss = {:.3f} at {}/{}.'.format(running_loss, i, n_iters),
              end='\r')

    print('')

    print('Evaluating model...')
    decoder.train(False)
    encoder.train(False)
    evaluations = []
    for (i, batch) in enumerate(val_dataloader):
        (image, input_labels, output_labels) = batch
        image = Variable(image.cuda())
        input_labels = Variable(input_labels.cuda())

        decoder.reset_state(batch_size=1)
        image_embedding = encoder(image)
        decoder.input_images(image_embedding)

        digit = input_labels[0, 0]
        sequence = []
        while len(sequence) < svhn.N_LABELS and digit.data[0] != svhn.STOP:
            prediction = decoder(digit)
            digit = torch.max(prediction, dim=1)[1]
            sequence.append(digit.data[0])

        while len(sequence) < svhn.N_LABELS:
            sequence.append(svhn.PAD)

        expected_sequence = output_labels[0].numpy().tolist()
        if sequence == expected_sequence:
            evaluations.append(1)
        else:
            evaluations.append(0)

    accuracy = float(sum(evaluations)) / float(len(evaluations))
    print('## Validation Accuracy = {:.3f}.'.format(accuracy))

print('Finished training. Testing the model!')

decoder.train(False)
encoder.train(False)
test_evaluations = []
for (i, batch) in enumerate(test_dataloader):
    (image, input_labels, output_labels) = batch
    image = Variable(image.cuda())
    input_labels = Variable(input_labels.cuda())

    decoder.reset_state(batch_size=1)
    image_embedding = encoder(image)
    decoder.input_images(image_embedding)

    digit = input_labels[0, 0]
    sequence = []
    while len(sequence) < svhn.N_LABELS and digit.data[0] != svhn.STOP:
        prediction = decoder(digit)
        digit = torch.max(prediction, dim=1)[1]
        sequence.append(digit.data[0])

    while len(sequence) < svhn.N_LABELS:
        sequence.append(svhn.PAD)

    expected_sequence = output_labels[0].numpy().tolist()
    if sequence == expected_sequence:
        test_evaluations.append(1)
    else:
        test_evaluations.append(0)

accuracy = float(sum(test_evaluations)) / float(len(test_evaluations))
print('## Test Accuracy = {:.3f}.'.format(accuracy))
