from torch.utils.data import Dataset
import cv2
import numpy as np
from torchvision.transforms import functional
import random

class SegDataset(Dataset):
    def __init__(self, traintxt, imagesize, cropsize, transfrom=None):
        self.images = []
        self.labels = []

        lines = open(traintxt, 'r').readlines()
        for line in lines:
            imagepath, labelpath = line.strip().split(' ')
            self.images.append(imagepath)
            self.labels.append(labelpath)

        self.imagesize = imagesize
        self.cropsize = cropsize

        assert len(self.images) == len(self.labels)
        self.transform = transfrom
        self.samples = []
        for i in range(len(self.images)):
            self.samples.append((self.images[i], self.labels[i]))

    def __getitem__(self, item) -> tuple:
        img_path, label_path = self.samples[item]
        img = cv2.imread(img_path)
        img = cv2.resize(img, (self.imagesize, self.imagesize), interpolation=cv2.INTER_NEAREST)
        label = cv2.imread(label_path, 0)
        label = cv2.resize(label, (self.imagesize, self.imagesize), interpolation=cv2.INTER_NEAREST)

        randoffsetx = np.random.randint(self.imagesize-self.cropsize)
        randoffsety = np.random.randint(self.imagesize-self.cropsize)
        img = img[randoffsety:randoffsety+self.cropsize, randoffsetx:randoffsetx+self.cropsize]
        label = label[randoffsety:randoffsety+self.cropsize, randoffsetx:randoffsetx+self.cropsize]
        #or use
        # img, label = self._segmentation_transforms(self, img, label)

        if self.transform is not None:
            img = self.transform(img)
        return img, label
    
    def __len__(self):
        return len(self.images)
    
    def _segmentation_transforms(self, image, mask):
        if random.random()>0.5:
            rangle = random.randint(-30,30)
            image = functional.rotate(image, angle=rangle)
            mask = functional.rotate(mask, angle=rangle)
        return image, mask