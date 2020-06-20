from tkinter import *
from subprocess import *
#import tkinter as tk
#from PIL import Image,ImageTk
#import speak
#speak.explain()

root = Tk()

root.title("Attendance Manager")

def openx():
    Popen('python click__pictures.py')


root.title("Attendence Manager")
canvas = Canvas(root, width=800, height=500)
canvas.pack()
photo = PhotoImage(file="main//bk.png")
canvas.create_image(180, 280, image=photo)


photo_1 = PhotoImage(file = r"name.png")
photoimage = photo_1.subsample(3, 2)
button_1 = Button(root, text="Enter Name", image = photo_1,command=openx, highlightthickness = 0, bd = 0)
label_a = canvas.create_window(90, 180, anchor='nw', window=button_1)

photo_2 = PhotoImage(file = r"training.png")
photoimage = photo_2.subsample(2, 2)
button_2 = Button(root, text="Training",image = photo_2, command=lambda:exec(open('face_recognition1.py').read()),highlightthickness = 0, bd = 0)
label_a = canvas.create_window(310,90, anchor='nw', window=button_2)

photo_3 = PhotoImage(file = r"face.png")
photoimage = photo_3.subsample(2, 2)
button_3 = Button(root, text="Face Recognize",image = photo_3, command=lambda:exec(open('face_recognition.py').read()),highlightthickness = 0, bd = 0)
label_a = canvas.create_window(520, 190, anchor='nw', window=button_3)

root.mainloop()
