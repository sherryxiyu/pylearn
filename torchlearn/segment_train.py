
from torchvision import transforms
import torch.nn as nn
from torch.optim import lr_scheduler, SGD
from torchvision import datasets,models,transforms
import os
from segment_net import simpleNet5
from segment_dataset import SegDataset
from torch.utils.data import DataLoader
import numpy as np
import torch

# writer = SummaryWriter()
batchsize = 64
epochs = 200
imagesize = 256
cropsize = 224
train_data_path = 'data/train.txt'
val_data_path = 'data/val.txt'

data_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])
])

train_dataset = SegDataset(train_data_path, imagesize, cropsize, data_transform)
train_dataloader = DataLoader(train_dataset, batch_size=batchsize, shuffle=True)
val_dataset = SegDataset(val_data_path, imagesize, cropsize, data_transform)
val_dataloader = DataLoader(val_dataset, batch_size=val_dataset.__len__(), shuffle=True)

image_datasets = {}
image_datasets['train'] = train_dataset
image_datasets['val'] = val_dataset
dataloaders = {}
dataloaders['train'] = train_dataloader
dataloaders['val'] = val_dataloader

device = torch.device('cpu')
net = simpleNet5().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = SGD(net.parameters(), lr=1e-1, momentum=0.9)
scheduler = lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.1)

if not os.path.exists('checkpoints'):
    os.mkdir('checkpoints')

for epoch in range(1, epochs+1):
    print(f"Epoch {epoch}/{epochs-1}")
    for phase in ['train', 'val']:
        if phase == 'train':
            scheduler.step()
            net.train(True)
        else:
            net.train(False)

        running_loss = 0.0
        running_accs = 0.0

        n=0
        for data in dataloaders[phase]:
            imgs, labels = data
            img, label = imgs.to(device).float(), labels.to(device).float()
            output = net(img)
            loss = criterion(output, label.long())

            output_mask = output.cpu().data.numpy().copy()
            output_mask = np.argmax(output_mask, exis=1)
            y_mask = label.cpu().data.numpy().copy()
            acc = (output_mask == y_mask)
            acc = acc.mean()

            optimizer.zero_grad()
            if phase == 'train':
                loss.backward()
                optimizer.step()

            running_loss += loss.data.item()
            running_loss += acc
            n+=1

        epoch_loss = running_loss / n
        epoch_acc = running_accs / n

        if phase == 'train':
            # writer.add_scaler('data/trainloss', epoch_loss, epoch)
            # writer.add_scaler('date/trainacc', epoch_acc, epoch)
            print(f"train epoch_{epoch} loss={epoch_loss}")
            print(f"train epoch_{epoch} acc={epoch_acc}")
        else:
            print(f"val epoch_{epoch} loss={epoch_loss}")
            print(f"val epoch={epoch} acc={epoch_acc}")

    if epoch % 10==0:
        torch.save(net, f"checkpoints/model_epoch_{epoch}.pth")
        print(f'checkpoints/model_epoch_{epoch}.pth saved!')

# writer.export_scalars_to_json("./all_scalars.json")
# wtirer.close()