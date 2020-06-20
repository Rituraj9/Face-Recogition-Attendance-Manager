# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:42:17 2020

@author: Rituraj
"""

import cv2
import os
import numpy as np
from PIL import Image
import pickle 
#import speech_recognition as sr #pip install speechRecognition
import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir,"images1")

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
speak("Let's Train Our Model...")
speak("Training...")
current_id=0
label_ids ={}
y_labels = []
x_train=[]

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ","-").lower()
            #print(label,path)
            if not label in label_ids:
                label_ids[label]=current_id
                current_id+=1
            id_ =label_ids[label]
            #print(label_ids)
            
           # y_labels.append(label)
           # x_train.append(path)
            
            pil_image = Image.open(path).convert("L")
            size=(650,650)
            final_image=pil_image.resize(size,Image.ANTIALIAS)
            image_array = np.array(final_image,"uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array,1.5,5)
            
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

#print(y_labels)
#print(x_train)
                
with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)
    
speak("Trained Successfully!! Ready to Recognise Faces..!!")
recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")