from torch import nn
import torch

class simpleNet5(nn.Module):
    def __init__(self):
        super(simpleNet5, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1),
            nn.BenchNorm2d(32),
            nn.ReLU(True),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.BenchNorm2d(64),
            nn.ReLU(True),
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.BenchNorm2d(128),
            nn.ReLU(True),
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.BenchNorm2d(256),
            nn.ReLU(True),
        )
        self.conv5 = nn.Sequential(
            nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1),
            nn.BenchNorm2d(512),
            nn.ReLU(True),
        )

        self.deconv1 = nn.Sequential(
            nn.ConvTranspose2d(512, 256, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BenchNorm2d(256),
            nn.ReLU(True),
        )
        self.deconv2 = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BenchNorm2d(128),
            nn.ReLU(True),
        )
        self.deconv3 = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BenchNorm2d(64),
            nn.ReLU(True),
        )
        self.deconv4 = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BenchNorm2d(32),
            nn.ReLU(True),
        )
        self.deconv5 = nn.Sequential(
            nn.ConvTranspose2d(32, 8, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BenchNorm2d(8),
            nn.ReLU(True),
        )

        self.classifier = nn.Conv2d(8, 3, kernel_size=1)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(x)
        out = self.conv3(x)
        out = self.conv4(x)
        out = self.conv5(x)
        out = self.deconv1(x)
        out = self.deconv2(x)
        out = self.deconv3(x)
        out = self.deconv4(x)
        out = self.deconv5(x)
        out = self.classifier(out)
        return out
    
if __name__ == "__main__":
    img = torch.randn(3, 3, 224, 224)
    net = simpleNet5()
    sample = net(img)
    print(sample.shape)
