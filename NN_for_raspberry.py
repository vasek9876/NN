from tkinter import *
from tkinter import filedialog
from Constants import *

master = Tk()
master.title("NN menu")
master.geometry(str(width) + "x" + str(height))

class NN:
    def __init__(self):
        from Scripts.AI import init_params
        self.data = init_params() #w1,b1,w2,b2,w3,b3...
    def setup_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def learn(self):
        import Scripts.Data as Data
        # get all of data (X.shape = (n:240:320), Y.shape = (n:1:6))
        X, Y = Data.read()
        print("Sample data count:", len(X))
        # print(Y)

        from Scripts.AI import gradient_descent as train

        alpha = 0.10
        iterations = 100
        print("alpha:", alpha, "iterations", iterations)

        self.data = train(self.data, X, Y, alpha, iterations)
    def test(self):
        import Scripts.Data as Data
        # get all of data (X.shape = (n:240:320), Y.shape = (n:1:6))
        X, Y = Data.read()

        import Scripts.AI as AI

        X, Y_train = X, Y
        # must be between 0 and 1
        X_train = X / 255
        iterations = 100
        W1, b1, W2, b2, W3, b3 = self.data
        for i in range(iterations):
            X_ = X_train[i].flatten()
            Z1, A1, Z2, A2, Z3, A3 = AI.forward_prop(W1, b1, W2, b2, W3, b3, X_)
            print(AI.get_accuracy(A3,Y[i]))
    def classify(self):

        import Sample_data.CSV_generator as classify


        #path =
        #print(path)
        classify.run(local + "/" + PATH["Sample_data"], Toplevel())

class nav_bar:
    def __init__(self):


        # init NN
        self.NN = NN()

        # set menu
        self.menu = Menu(master)

        # file
        self.file = Menu(self.menu, tearoff=0)

        self.file.add_command(label="Re-Open NN data", command=self.open_NN_data)
        self.file.add_command(label="Save as NN data", command=self.save_data)
        self.file.add_separator()  # -----#
        self.file.add_command(label="Exit", command=quit)

        # run
        self.run = Menu(self.menu, tearoff=0)

        self.run.add_command(label="Neural network learning", command=self.NN.learn)
        self.run.add_command(label="Neural network testing", command=self.NN.test)
        self.run.add_separator()  # -----#
        self.run.add_command(label="Classify data", command=self.NN.classify)

        # init
        self.menu.add_cascade(menu = self.file, label="File")
        self.menu.add_cascade(menu = self.run, label="Run")

        # master init
        master.config(menu=self.menu)





        # try to init data of NN
        self.open_NN_data()
    def open_NN_data(self):
        try:
            data = list()
            for file in (NN_architecture[:-1]):
                path = PATH["NN_data"] + "/" + file + "." + NN_architecture[-1]
                with open(path, "r") as f:
                    for line in f:
                        data.append(line.split(";"))
            print(data[-1])
            self.NN.setup_data(data)
        except:
            print("File does not exist, so start the learning.")




        #master.filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=(
        #("stx files", "*.stx"), ("txt files", "*.txt"), ("all files", "*.*")))

        #lineList = [line.rstrip('\n') for line in open(master.filenames)].split(";")



    def save_data(self):
        pass






if __name__ =="__main__":
    nav_bar()
    mainloop()
