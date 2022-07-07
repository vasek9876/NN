"""
class with append mode to add new input and output csv


data [(X,Y),(X,Y)...]
X = [(320x240), (320x240)...]
Y = [(1x6),(1x6)...]
"""
import numpy as np

"""
X,Y Input and Output 
x,y Read data as new csv
"""
def add_dataset(X,Y,x,y):
    X=np.concatenate((X,[x]))
    Y=np.concatenate((Y,[y]))
    return X,Y

def shuffle(X,Y):
    data = list()
    for x,y in zip (X,Y):
        data.append([x,y])
    #data = np.array(data)
    np.random.shuffle(data)
    X = list()
    Y = list()
    for x,y in (data):
        X.append(x)
        Y.append(y)
    X = np.array(X)
    Y = np.array(Y)
    return X,Y
