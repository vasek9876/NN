"""
NN main file
"""

#geting DATA
import Scripts.Data as Data
# get all of data (X.shape = (n:240:320), Y.shape = (n:1:6))
X,Y = Data.read()
print("Sample data count:", len(X))
#print(Y)


from Scripts.AI import gradient_descent as train



alpha = 0.12
iterations = 100

W1, b1, W2, b2, W3, b3 = train(X,Y,alpha,iterations)

import numpy as np
import Scripts.AI as AI

X,Y_train = X,Y
#must be between 0 and 1
X_train = X/255
iterations = 100
for i in range(iterations):
    X_ = X_train[i].flatten()
    Z1, A1, Z2, A2, Z3, A3 = AI.forward_prop(W1, b1, W2, b2, W3, b3, X_)
    print(AI.get_accuracy(A3, Y))
    #print(A3,Y[i])



