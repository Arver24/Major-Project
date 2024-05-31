import torch
import torch.nn as nn
import torch.optim as optim


class DNN(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(1, 192)
        self.act1 = nn.ReLU()
        self.layer2 = nn.Linear(192, 96)
        self.act2 = nn.ReLU()
        self.layer3 = nn.Linear(96, 96)
        self.act3 = nn.ReLU()
        self.output = nn.Linear(96, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.act1(self.layer1(x))
        x = self.act2(self.layer2(x))
        x = self.act3(self.layer3(x))
        x = self.sigmoid(self.output(x))
        return x
