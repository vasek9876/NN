from tkinter import *
from PIL import Image, ImageTk


print("ctrl+space to setup the image - do not save csv, ctrl+tab for next save csv")

def run(path, window):
    def try_to_open(file):
        try:
            with open(file, "r") as f:
                n.set("".join(f.read().split(";")))


        except Exception as e:
            n.set("")
            print("Has not classify yet.")
    n = StringVar()
    n.set("")
    last_l = Label(window, textvariable=n)
    last_l.pack()

    window.focus_set()
    window.grab_set()
    name = path+"/Output"
    name_input = path+"/Input"

    file_type_input = ".jpg"
    file_type = ".csv"
    global num
    num = 0

    # entry box
    my_input = Entry(window)
    my_input.pack()
    my_input.focus()

    # num entry
    s=StringVar()
    s.set(str(num))
    label = Entry(window, textvariable=s, )
    label.pack()





    i = ImageTk.PhotoImage(Image.open(name_input + str(num) + file_type_input))
    img = Label(window, image=i)
    img.pack()
    img.configure(image=i)
    img.image = i

    try_to_open(name + str(num) + file_type)


    def reopen(event):
        global num
        if int(label.get()) == num:
            num+=1
        else:
            num = int(label.get())
        i = ImageTk.PhotoImage(Image.open(name_input + str(num) + file_type_input))
        img.configure(image=i)
        img.image = i
        my_input.focus()

        s.set(str(num))

        try_to_open(name + str(num) + file_type)


    def classify(event):
        global num
        data = ";".join(list(my_input.get()))  # replace("", ";")

        print(num, "DATA:", data)
        f = open(name + str(num) + file_type, "w+")
        f.write(data)
        f.close()

        num += 1

        s.set(str(num))


        i = ImageTk.PhotoImage(Image.open(name_input + str(num) + file_type_input))
        img.configure(image=i)
        img.image = i
        my_input.focus()

        try_to_open(name + str(num) + file_type)



    window.bind('<Control-s>',classify)
    window.bind('<Control-space>', reopen)




if __name__=="__main__":


    window = Tk()
    window.geometry("250x100")
    run(".", window)
    window.mainloop()
