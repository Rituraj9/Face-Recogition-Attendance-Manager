# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:42:56 2020

@author: Rituraj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:57:38 2020

@author: Rituraj
"""

import cv2
#import name
import os

#print('hi')
#na = 
#print(na)
from tkinter import *
from PIL import ImageTk, Image

import tkinter
from tkinter import ttk
import pyttsx3 #pip install pyttsx3

window = tkinter.Tk()
window.title("User Input")
canvas = Canvas(window, width=250, height=250)
canvas.pack()
photo = PhotoImage(file="main\\pic2.png")
canvas.create_image(125, 125, image=photo)


# my_img = tkinter.PhotoImage(
#     file="C:\\Users\\Abhinav\\Downloads\\opencv-master\\opencv-master\\samples\\data\\rubberwhale2.png")
# my_label = tkinter.Label(window, image=my_img)  # .pack()
# my_label.grid(row=4, column=4)

label = ttk.Label(window, text="Enter Your name ",anchor='w')
label_a = canvas.create_window(75, 25, anchor='nw', window=label)

username = tkinter.StringVar()

userentry = ttk.Entry(window, width=26, textvariable=username)
label_b = canvas.create_window(45, 60, anchor='nw', window=userentry)


def action():
    return username.get()


btn = ttk.Button(window, text="Submit", command=action)
label_c = canvas.create_window(75, 100, anchor='nw', window=btn)

label = ttk.Label(window, text="(Close Dialog Box)",anchor='w')
label_a = canvas.create_window(55, 125, anchor='nw', window=label)
window.mainloop()

na = action()
print(na)
path = 'images1'
os.chdir(path)
new = na
os.mkdir(new)

count=0
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

while True:
    success,img = cap.read()
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("images1/"+new+"/"+str(count)+".jpg",img)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,0),2)
        cv2.imshow("Image",img)
        cv2.waitKey(500)
        count+=1
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()