import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn import preprocessing
import pandas as pd
import pickle as cPickle
import gzip

def npSoftmax(X):
    e = np.exp(X)
    return e/np.sum(e,axis=0)


def npLRelu(X):
    return np.maximum(0.01*X,X)


def dLRel(X):
    return np.maximum(0.01, X/np.abs(X))


def npSigmoid(X):
    return 1 / (1 + np.exp(-1 * X))


def para_init(num_nodes):
    wt = {}
    for l in range(1,len(num_nodes)):
        wt["W" + str(l)] = np.random.standard_normal([num_nodes[l], num_nodes[l-1]])/num_nodes[l-1]
        wt["b" + str(l)] = np.zeros((num_nodes[l],1))

    return wt


def forward_prop(Wts, X, l):
    z_dict = {}
    a_dict = {}
    # print("forward prop")
    a_dict["A0"] = X
    for i in range (1,l-1):
        z_dict["Z" + str(i)] = np.dot(Wts["W" + str(i)], a_dict["A" + str(i-1)]) + Wts["b" + str(i)]
        a_dict["A" + str(i)] = npLRelu(z_dict["Z" + str(i)])

    z_dict["Z" + str(l-1)] = np.dot(Wts["W" + str(l-1)], a_dict["A" + str(l-2)]) + Wts["b" + str(l-1)]
    a_dict["A" + str(l-1)] = npSigmoid(z_dict["Z" + str(l-1)])

    return a_dict, z_dict


def update(Wts, Z_Dict, A_Dict, Y, l, m, lr):
    der_dict = {}
    # print("Updating")
    der_dict["dZ" + str(l-1)] = A_Dict["A" + str(l-1)] - Y
    der_dict["dW" + str(l-1)] = (1/m)*np.dot(der_dict["dZ" + str(l-1)], A_Dict["A" + str(l-2)].T)
    der_dict["db" + str(l-1)] = (1/m)*np.sum(der_dict["dZ" + str(l-1)], axis = 1)
    l = l-1
    for i in range (1,l) :
        der_dict["dZ" + str(l-i)] = np.dot(Wts["W" + str(l-i+1)].T, der_dict["dZ" + str(l-i+1)])*dLRel(Z_Dict["Z" + str(l-i)])
        der_dict["dW" + str(l-i)] = (1/m)*np.dot(der_dict["dZ" + str(l-i)], A_Dict["A" + str(l-i-1)].T)
        der_dict["db" + str(l-i)] = (1/m)*np.sum(der_dict["dZ" + str(l-i)], axis = 1)


    for i in range(1,l) :
        Wts["W" + str(i)] = Wts["W" + str(i)] - lr*der_dict["dW" + str(i)]
        Wts["b" + str(i)] = Wts["b" + str(i)] - lr*der_dict["db" + str(i)]

    return Wts


def cost(Al, Y):
    J = np.sum(np.power((Al-Y),2))
    # print("finding cost")
    c = np.sum(J)/(2*Y.shape[1])
    return c


def prediction(Al, Ynum):
    arg = np.argmax(Al,axis=0)
    arg = arg.reshape(1,Ynum.shape[1])
    # print(arg.shape, Ynum.shape)
    cnt = 0
    # print("predicting")
    for i in range(Ynum.shape[1]):
        if(arg[0,i]==Ynum[0,i]):
            cnt = cnt+1
    return (cnt/Ynum.shape[1])


def learn(Wts, lr, num_iter, X, Y, Ynum, k, show):
    l = len(layer_dims)
    m = X.shape[1]
    costs = []

    for i in range(num_iter):
        A_Dict, Z_Dict = forward_prop(Wts, X, l)
        # print(i)
        costs.append(cost(A_Dict["A" + str(l-1)], Ynum))
        Wts = update(Wts, Z_Dict, A_Dict, Y, l, m, lr)

    if show:
        predict = prediction(A_Dict["A" + str(l-1)], Ynum)
        print("Cost is : ", costs[i])
        percent = np.sum(np.abs(predict))
        print("Percentage Accuracy after", k, "epochs is : ", percent*100)

    return Wts



# with open('mnist.pkl') as f:
#     data = pickle.load(f)
data = gzip.open("/media/khurshed2504/Data/PycharmProjects/ML_temp0/mnist.pkl.gz")
train_data,  validation_data, test_data = cPickle.load(data,encoding="latin1")
X = train_data[0]
X = X.T
print(X.shape)
n_X = X.shape[0]
m = X.shape[1]
X_broke = np.zeros((X.shape[0], 100))

Ynum = train_data[1]
print("Ynum Shape (Native) : ", Ynum.shape)
Ynum = Ynum.reshape(1, Ynum.shape[0])
print("Ynum Shape (After Reshape) : ", Ynum.shape)
print(Ynum)

Y = np.eye(10)[Ynum]
print(Y.shape)
Y = Y.squeeze()
print(Y.shape)
Y = Y.reshape(10,m)
# le = preprocessing.LabelEncoder()
# Y = Ynum.apply(le.fit_transform)

# Y = np.zeros((10,Ynum.shape[1]))
# j=0
# for i in Ynum :
#     Y[i,j] = 1
#     j = j+1
#
# print("Y shape", Y.shape)
# print(Y)

layer_dims = [n_X,300,300,300,10]
Wts = para_init(layer_dims)
for i in range (500):
    X_broke = X[:,100*i:100*(i+1)]
    Y_broke = Y[:, 100 * i:100 * (i + 1)]
    Ynum_broke = Ynum[:, 100 * i:100 * (i + 1)]
    Wts = learn(Wts, 0.002, 50, X_broke, Y_broke, Ynum_broke, i, show=True)

# Wt = learn(layer_dims, 0.012, 10000, X, Y, Ynum, 1, show=True)