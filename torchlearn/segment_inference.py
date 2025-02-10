import torch
from torchvision import transforms
import os
import cv2
import sys
import torch.nn.functional as F
import numpy as np

data_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])
])

modelpath = sys.argv[1]
net = torch.load(modelpath, map_location='cpu')
net.eval()

imagepaths = os.listdir()
torch.no_grad()
for imagepath in imagepaths:
    image = cv2.imread(os.path.join(sys.argv[2], imagepath))
    image = cv2.resize(image, (224,224), interpolation=cv2.INTER_NEAREST)
    imgblob = data_transforms(image, (224,224), interpolation=cv2.INTER_NEAREST)
    predict = F.softmax(net(imgblob)).cpu().data.numpy().copy()
    predict = np.argmax(predict, axis=1)
    result = np.squeeze(predict)
    print(np.max(result))

    resultimage = image.copy()
    for y in range(0, result.shape[0]):
        for x in range(0, result.shape[1]):
            if result[y][x] == 127:
                resultimage[y][x] = (0,0,255)
            elif result[y][x] == 254:
                result[y][x] = (0,255,255)

    combineresult = np.concatenate([image, resultimage], axis=1)
    cv2.imwrite(os.path.join(sys.argv[3], imagepath), combineresult)