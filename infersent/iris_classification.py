import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import torch.optim as optim
import torch.nn as nn
import torch
import numpy as np
import pandas as pd
from infersent.neural_net import Net
import random
from torch.autograd import Variable

net = Net()
loss = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.003)
dataset = pd.read_csv("da.csv")
dataset.loc[dataset.species == 'Iris-setosa', 'species'] = 0
dataset.loc[dataset.species == 'Iris-versicolor', 'species'] = 1
dataset.loc[dataset.species == 'Iris-virginica', 'species'] = 2


# wrap up with Variable in pytorch
train_X = list(dataset[dataset.columns[0:4]].values)
test_X = list(dataset[dataset.columns[0:4]].values)

train_Y = list(dataset.species.values)

for i, j in enumerate(train_Y):
    if j == 0:
        train_Y[i] = [1.0, 0.0, 0.0]
    if j == 1:
        train_Y[i] = [0.0, 1.0, 0.0]
    if j == 2:
        train_Y[i] = [0.0, 0.0, 1.0]

train_y =train_Y
test_y = train_Y

optimizer = torch.optim.SGD(net.parameters (), lr = 0.003)

for epoch in range(20000):
    optimizer.zero_grad()
    out = net(Variable(torch.Tensor(train_X)))
    # print(out, torch.Tensor(train_y))
    loss1 = loss(out, torch.Tensor(train_y))
    loss1.backward()
    optimizer.step()

    if epoch % 100 == 0:
        # print (out, torch.Tensor (train_y))
        print ('number of epoch', epoch, 'loss', loss1)