import numpy as np
import pickle as cPickle
import gzip



def npRelu(X):
    return np.maximum(0,X)



def npLRelu(X):
    return np.maximum(0.01*X,X)



def dLRel(X):
    return np.maximum(0.01, X/np.abs(X))



def npSigmoid(X):
    return 1 / (1 + np.exp(-1 * X))



def npSoftmax(X):
    e = np.exp(X)
    return e/np.sum(e,axis=0)


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


def para_init():
    W1 = np.random.randn(300, 784)*0.01
    b1 = np.zeros((300, 1))

    W2 = np.random.randn(200, 300)*0.01
    b2 = np.zeros((200, 1))

    W3 = np.random.randn(10,200)*0.01
    b3 = np.zeros((10, 1))

    return W1, W2, W3, b1, b2, b3



def forward_prop(W1, W2, W3, b1, b2, b3, X):
    Z1 = np.dot(W1, X) + b1
    A1 = npLRelu(Z1)

    Z2 = np.dot(W2, A1) + b2
    A2 = npLRelu(Z2)

    Z3 = np.dot(W3, A2) + b3
    A3 = npSoftmax(Z3)

    return Z1, Z2, Z3, A1, A2, A3



def update(W1, W2, W3, b1, b2, b3, Z1, Z2, Z3, A1, A2, A3, X, Y, lr):
    m = Y.shape[1]

    dZ3 = A3 - Y
    dW3 = np.dot(dZ3, A2.T)/m
    db3 = np.sum(dZ3, axis = 1).reshape(10,1)/m

    dZ2 = np.dot(W3.T, dZ3)*dLRel(Z2)
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, axis = 1).reshape(200,1)/m

    dZ1 = np.dot(W2.T, dZ2)*dLRel(Z1)
    dW1 = np.dot(dZ1, X.T)/m
    db1 = np.sum(dZ1, axis = 1).reshape(300,1)/m

    W3 = W3 - lr*dW3
    b3 = b3 - lr*db3

    W2 = W2 - lr*dW2
    b2 = b2 - lr*db2

    W1 = W1 - lr*dW1
    b1 = b1 - lr*db1

    return W1, W2, W3, b1, b2, b3



def learn(W1, W2, W3, b1, b2, b3, X, Y, Ynum, k, lr, num_iter, show):

    for i in range(num_iter+1):
        Z1, Z2, Z3, A1, A2, A3 = forward_prop(W1, W2, W3, b1, b2, b3, X)
        W1, W2, W3, b1, b2, b3 = update(W1, W2, W3, b1, b2, b3, Z1, Z2, Z3, A1, A2, A3, X, Y, lr)
    print("done")
    arg = np.argmax(A3,axis=0)
    percent = prediction(A3, Ynum)
    print("Epochs completed : ", k + 1)
    print("Percent Accuracy : ",percent*100)
    print("Learning Rate is : ", lr)
    return W1, W2, W3, b1, b2, b3





data = gzip.open("/media/khurshed2504/Data/PycharmProjects/ML_temp0/mnist.pkl.gz")
train_data,  validation_data, test_data = cPickle.load(data,encoding="latin1")


X = train_data[0]
X = X.T
print("X Shape : ",X.shape)
n_X = X.shape[0]
m = 1000

Ynum = train_data[1]
print("Ynum Shape (Native) : ", Ynum.shape)
Ynum = Ynum.reshape(1, Ynum.shape[0])
print("Ynum Shape (After Reshape) : ", Ynum.shape)
print(Ynum)

Y = np.eye(10)[Ynum]
print(Y.shape)
Y = Y.squeeze()
print(Y.shape)
Y = Y.reshape(10,50000)
# print("Final Y Shape : ", Y1.shape)

W1, W2, W3, b1, b2, b3 = para_init()

for i in range(50):
    Y1 = np.array(Y[:, m*(i):m*(i+1)]).reshape(10, 1000)
    X1 = np.array(X[:, m*(i):m*(i+1)]).reshape(784, 1000)
    Ynum1 = np.array(Ynum[:, m * (i):m * (i + 1)]).reshape(1, 1000)
    W1, W2, W3, b1, b2, b3 = learn(W1, W2, W3, b1, b2, b3, X1, Y1, Ynum1, i, 0.01, num_iter = 100, show = True)