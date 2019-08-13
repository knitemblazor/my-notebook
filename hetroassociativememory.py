import numpy as np


class NeuralNet:
    def __init__(self):
        funct = "neural net hebbian rule"
        self.funct = funct

    @staticmethod
    def network(train_x, train_y):
        # feature_vector = np.array([-.5] * inp)
        feature_vector = [0.5, .26, -.23, 2, .32, -2.4, 0.5, .26, -.23, 9]
        # mean = [0, 0]
        # cov = [[1, 0], [0, 100]]  # diagonal covariance
        # x, y = np.random.multivariate_normal(mean, cov, inp*out).T
        # weight_matrix = x.reshape(inp, out)
        # print(weight_matrix)
        weight_matrix = np.array([[0] * len(train_y[1])] * len(train_x[1]))
        # np.dot(np.array([1,2,3,4]).reshape(4,1), np.array([1,2]).reshape(1,2))
        # np.matmul(np.array(train_x[1]).reshape(5,1),np.array(train_y[1]).reshape(1,2))
        noofepochs = 4
        for i in range(noofepochs):
            for j in range(len(train_x)):
                p = np.matmul(np.array(train_x[j]).reshape(len(train_x[1]), 1), np.array(train_y[j]).reshape(1, len(train_y[1])))
                weight_matrix = weight_matrix + p
        # counter = 0
        # while list(output_vector) != list(feature_vector):
        #     weight_matrix = weight_matrix + np.matmul(np.transpose(feature_vector), output_vector)
        #     output_vector = np.matmul(weight_matrix, np.transpose(feature_vector))
        #     output_vector1 = []
        #     for i in output_vector:
        #         if i < 0:
        #             j = -1
        #             output_vector1.append(j)
        #         elif i == 0:
        #             j = 0
        #             output_vector1.append(j)
        #         elif i > 0:
        #             j = 1
        #             output_vector1.append(j)
        #     output_vector = output_vector1
        #     print(weight_matrix, feature_vector, output_vector)
        #     counter = counter + 1

        return weight_matrix


train_set_X = [[1, 0, 1, 0, 0],
               [0, 1, 1, 0, 0],
               [0, 0, 0, 1, 1],
               [0, 0, 0, 1, 0]]

train_set_y = [[1, 0],
               [1, 0],
               [0, 1],
               [0, 1]]

a=NeuralNet.network(train_set_X, train_set_y)
print(a)
