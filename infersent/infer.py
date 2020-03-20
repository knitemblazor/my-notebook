import torch
import numpy as np
import pandas as pd
from infersent.model import InferSent
from infersent.neural_net import Net
import torch.optim as optim
import torch.nn as nn
import random
from torch.autograd import Variable

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

loss = nn.BCELoss()
net = Net()
optimizer = optim.Adam(net.parameters(), lr=0.003)
df = pd.read_csv("data.csv")
df = df.sample(frac=1).reset_index(drop=True)
model_version = 1
MODEL_PATH = "encoder/infersent%s.pkl" % model_version
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': model_version}
model = InferSent(params_model)
model.load_state_dict(torch.load(MODEL_PATH))
W2V_PATH = 'encoder/GloVe/glove.840B.300d.txt' if model_version == 1 else 'encoder/fastText/crawl-300d-2M.vec'
model.set_w2v_path(W2V_PATH)
model.build_vocab_k_words(K=100000)
text = list(df["0"])
lab = list(df["1"])

labelx = []
for label in lab:
    inter = [0.0 for i in range(4)]
    inter[label] = 1.0
    labelx.append(inter)


text_fin = []
for i in range (len(text)):
    text_fin.append(model.encode([text[i]])[0])
    print("count: %d" %i)
text_fin = np.array(text_fin)


# print(text)



def error_function(inp,out):
    return 1/(np.dot(inp, out) / (np.linalg.norm(inp) * np.linalg.norm(out)))

def train_pytorch(text, labelx):
    # net.load_state_dict (torch.load ("model.pth"))
    for i in range(1000):
        print("epoch: %d" % i)
        optimizer.zero_grad ()
        out = net(Variable(torch.Tensor(text_fin).float()))
        print(out, labelx)
        loss1 = loss(out, Variable(torch.Tensor(labelx).float()))
        print("loss:", round(loss1.item(), 3))
        loss1.backward ()
        optimizer.step ()
        print ("-------*--------")
        torch.save (net.state_dict(), "model.pth")
        print("model saved")

train_pytorch(text, labelx)

# text_fin = []
# for i in range (len(text)):
#     text_fin.append(model.encode([text[i]])[0])
# text_fin = np.array(text_fin)
#
# print(np.array(text_fin).shape)
#
#
# def baseline_model():
#     model = Sequential()
#     model.add(Dense(2048, input_dim=4096, activation='relu'))
#     model.add (Dense (1024, activation = 'relu'))
#     model.add(Dense(4, activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return model
#
#
# estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=16, verbose=1)
# kfold = KFold(n_splits=20, shuffle=True)
# results = cross_val_score(estimator, text_fin, labelx, cv=kfold)
# print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))