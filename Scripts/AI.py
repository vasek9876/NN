#ML run
#https://www.kaggle.com/code/wwsalmon/simple-mnist-nn-from-scratch-numpy-no-tf-keras/notebook


import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt

#flow
def init_params():
    W1 = np.random.rand(768, 76800) - 0.5
    b1 = np.random.rand(768, 1) - 0.5
    W2 = np.random.rand(192, 768) - 0.5
    b2 = np.random.rand(192, 1) - 0.5
    W3 = np.random.rand(4,192) - 0.5
    b3 = np.random.rand(4, 1) - 0.5
    #print(W1, b1, W2, b2, W3, b3)
    return W1, b1, W2, b2, W3, b3
#function
def ReLU(Z):
    #print(Z)
    return np.maximum(Z, 0.000001)
#function
def sigmoid(Z):
    if np.sum(Z)==0:
        return 0
    else:
        return 1 / (1 + np.exp(-Z))
#function
def softmax(Z):
    A = Z / np.sum(Z, axis=0)
    return A
#flow
def forward_prop(W1, b1, W2, b2, W3, b3, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = ReLU(Z2)
    Z3 = W3.dot(A2) + b3
    A3 = softmax(Z3)

    #print(X.shape, W1.shape, b1.shape, A1.shape ,A2.shape,A3.shape)
    #print((W1.dot(X) + b1).shape)
    return Z1, A1, Z2, A2, Z3, A3
#function
def ReLU_deriv(Z):
    return Z > 0
#function
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    #print(Y,one_hot_Y)
    return one_hot_Y[1]
#flow
def backward_prop(Z1, A1, Z2, A2, Z3, A3, W1, W2, W3, X, Y):
    m = 10000
    #print(Y.shape, np.array([one_hot(Y),]).T, A3)
    dZ3 = A3 - np.array([one_hot(Y),]).T
    dW3 = 1 / m * dZ3.dot(A2.T)
    db3 = 1 / m * np.sum(dZ3)
    
    dZ2 = W3.T.dot(dZ3) * ReLU_deriv(Z2)
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    #
    return dW1, db1, dW2, db2, dW3, db3
#flow
def update_params(W1, b1, W2, b2, W3, b3, dW1, db1, dW2, db2, dW3, db3, alpha):
    #print(W1[0]-alpha*dW1[0])
    W1 = W1 - alpha * dW1
    #b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    #b2 = b2 - alpha * db2
    W3 = W3 - alpha * dW3
    #b3 = b3 - alpha * db3
    return W1, b1, W2, b2, W3, b3
#function
def get_predictions(A3):
    return np.argmax(A3, 0)
#function
def get_accuracy(predictions, Y):
    return (str(predictions) + " -> " + str(np.array(Y)) + " % "+ "not Done!")
    #LR = predictions[0] > predictions[1]
    #FB = predictions[2] > predictions[3]
   #x = 0
    #x += (predictions[0]-predictions[1]) * LR * Y[0]*0.5
    #x += (predictions[1]-predictions[0]) * int(not LR) * Y[1]*0.5
    #x += (predictions[2]-predictions[3]) * FB * Y[2]*0.5
    #x += (predictions[3]-predictions[2]) * int(not FB) * Y[3]*0.5

    #return (str(predictions) + " -> " + str(np.array(Y)) + " % "+ str(x))


    #print(predictions, Y)
    #return np.sum(np.around(predictions == Y)) / Y.size
#flow
def gradient_descent(data, X, Y, alpha, iterations):
    X,Y_train = np.array(X),np.array(Y)
    #must be between 0 and 1
    X_train = X/255
    W1, b1, W2, b2, W3, b3 = data #init_params()
    for i in range(iterations):
        X_ = np.array([X_train[i].flatten(),]).T

        
        Z1, A1, Z2, A2, Z3, A3 = forward_prop(W1, b1, W2, b2, W3, b3, X_)

        dW1, db1, dW2, db2, dW3, db3 = backward_prop(Z1, A1, Z2, A2, Z3, A3, W1, W2, W3, X_, Y[i])
        W1, b1, W2, b2, W3, b3 = update_params(W1, b1, W2, b2, W3, b3, dW1, db1, dW2, db2, dW3, db3, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            #predictions = get_predictions(A3)
            #print(A3)
            print(get_accuracy(A3, Y[i]))
            
    return W1, b1, W2, b2, W3, b3


#train
#W1, b1, W2, b2, W3, b3 = gradient_descent(X_train, Y_train, 0.10, 500)
