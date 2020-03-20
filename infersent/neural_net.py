import torch
import torch.nn as nn


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.soft = nn.Softmax(dim = 1)
        self.fc1 = nn.Linear(4096, 2048)
        self.fc2 = nn.Linear(2048, 1024)
        self.fc3 = nn.Linear(1024, 512)
        self.fc4 = nn.Linear(512, 256)
        self.fc5 = nn.Linear(256, 4)


    def swish(self, x):
        return x*torch.sigmoid(x)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        x = torch.sigmoid(self.fc4(x))
        x = self.soft((self.fc5(x)))

        return x

# class Net(nn.Module):
#     # define nn
#     def __init__(self):
#         super(Net, self).__init__()
#         self.fc1 = nn.Linear(4, 100)
#         self.fc2 = nn.Linear(100, 100)
#         self.fc3 = nn.Linear(100, 3)
#         self.softmax = nn.Softmax(dim=1)
#
#     def forward(self, X):
#         X = torch.relu(self.fc1(X))
#         X = self.fc2(X)
#         X = self.fc3(X)
#         X = self.softmax(X)
#
#         return X
