import os

local = str(os.path.abspath(os.getcwd())).replace("\\","/")


width = 400
height = 400

PATH = {
    "Sample_data": "Sample_data",
    "NN_data": "NN_data",
    "Scripts": "Scripts",
}

NN_architecture = ("w1", "b1", "w2", "b2", "w3", "b3", "csv")
