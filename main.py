import tkinter
from tkinter import filedialog
from tkinter import*
from PIL import Image, ImageTk
from functools import partial
import shutil
from config import *
import os
from image_prep import*
import numpy as np
from matplotlib import cm
from skimage import data
import cv2
import image_prep
import make_prediction
import random



BACKGROUND_COLOR = "#EBE8E2"
INPUT_PATH = ""
OUTPUT_PATH = ""
MODEL_PATH = ""
CNN_MODEL = ""
BTN_HEIGHT = 4
BTN_WIDTH = 15
sem_image = None
def create_folders():
    """
    Creates folders for categories
    """
    if not os.path.exists(INPUT_FOLDER):
        os.mkdir(INPUT_FOLDER)
    if os.path.exists(OUTPUT_FOLDER):
        for path in PATHES:
            if not os.path.exists(path):
                os.mkdir(path)
    else:
        os.mkdir(f'{OUTPUT_PATH}\{OUTPUT_FOLDER}')
        for path in PATHES:
            os.mkdir(path)

def load_model(path):
    global CNN_MODEL
    if not path:
        CNN_MODEL = make_prediction.makePrediction(r'cnn_model')
    else:
        CNN_MODEL = make_prediction.makePrediction(path)
    return 0

def predict(file):
    file_path = r"input//"
    global CNN_MODEL,sem_image
    if not CNN_MODEL:
        return -1
    image = random_image(file_path)
    img_file = image_preprocessing.image_preprocess(image)
    create_img = ImageTk.PhotoImage(img_file)
    sem_image.configure(image=create_img)
    sem_image.image = create_img
    print(image)
    prediction = CNN_MODEL.make_predict(image) #assume all images are trimmed
    if prediction < 1:
        prediction_label.delete(0, END)
        prediction_label.insert(0, "Fail")
        prediction_label.config(bg="red")
    else:
        prediction_label.delete(0, END)
        prediction_label.insert(0, "Pass")
        prediction_label.config(bg="green")
    return prediction

def getPath(btn_name):
    global INPUT_PATH, OUTPUT_PATH, MODEL_PATH
    if btn_name =='output':
        OUTPUT_PATH = filedialog.askdirectory()
        output_path.delete(0,END)
        output_path.insert(0,OUTPUT_PATH)

    if btn_name =='input':
        INPUT_PATH = filedialog.askdirectory()
        input_path.delete(0,END)
        input_path.insert(0,INPUT_PATH)

    if btn_name =='model':
        MODEL_PATH = filedialog.askdirectory()
        model_path.delete(0,END)
        model_path.insert(0,MODEL_PATH)

def random_image(path):
    # if not INPUT_PATH:
    #     prediction_label.delete(0, END)
    #     prediction_label.insert(0, "EMPTY FOLDER")
    #     random_image  = r"images\white.jpg"
    #     return random_image
    random_image = f"{path}{random.choice(os.listdir(path))}"
    return random_image


if __name__ == '__main__':
    image_preprocessing = ImagePreProcessing()
    root = Tk()
    root.title('LMIS Image Classification')
    root.config(padx=20,pady=20, background= BACKGROUND_COLOR)
    frame = tkinter.Frame(root,background=BACKGROUND_COLOR)
    frame.pack()

    prediction_frame = tkinter.LabelFrame(frame,background=BACKGROUND_COLOR)
    prediction_frame.grid(row = 0 ,column=1,padx= 50,pady=50)

    prediction_label = tkinter.Entry(prediction_frame,font=('Georgia 20'),justify='center',bg='green')
    prediction_label.delete(0, END)
    prediction_label.insert(0, "Select image location")
    prediction_label.grid(row = 0,column=0,padx=20,pady=20)

    image_frame = tkinter.LabelFrame(frame,background= BACKGROUND_COLOR)
    image_frame.grid(row = 0,column = 0)

    file_path = r"images\white.jpg"
    img_file = image_preprocessing.image_preprocess(file_path)
    create_img = ImageTk.PhotoImage(img_file)
    sem_image = Label(image_frame, image = create_img)
    sem_image.grid(row = 0 ,column=0,padx=20,pady=20)

    button_frame = tkinter.LabelFrame(frame,background=BACKGROUND_COLOR)
    button_frame.grid(row=1,column = 0,padx=50,pady=50)

    load_model_btn = Button(button_frame,text="Load Model",command = partial(load_model,MODEL_PATH))
    load_model_btn.grid(row = 0,column = 0, rowspan = 2, columnspan=2, padx=20,pady=20)
    load_model_btn.config(heigh= BTN_HEIGHT,width=BTN_WIDTH)

    predict_btn = Button(button_frame, text = "Run Prediction",command = partial(predict,INPUT_PATH))
    predict_btn.grid(row = 0 ,column=3,rowspan= 2,columnspan=2, padx=20,pady=20)
    predict_btn.config(heigh=BTN_HEIGHT, width=BTN_WIDTH)

    predict_batch_btn = Button(button_frame,text = "Batch Prediction")
    predict_batch_btn.grid(row = 0, column=5,rowspan=5,columnspan=5,padx=20,pady=20)
    predict_batch_btn.config(heigh=BTN_HEIGHT, width=BTN_WIDTH)

    file_frame= tkinter.LabelFrame(frame,background=BACKGROUND_COLOR)
    file_frame.grid(row =1,column=1,padx= 50,pady=50)

    folder_photo = PhotoImage(file = r"images\folder_icon.png").subsample(100,100)

    input_path_label = tkinter.Label(file_frame, text='Input Path:', background=BACKGROUND_COLOR)
    input_path_label.grid(row=0, column=0, padx=5, pady=20)
    input_path = tkinter.Entry(file_frame,width=50)
    input_path.grid(row = 0,column = 1,padx=20,pady=20, columnspan=40)
    input_folder_button = Button(file_frame,image = folder_photo, command = partial(getPath,'input'))
    input_folder_button.grid(row = 0, column=41,padx=5,pady=20)

    output_path_label = tkinter.Label(file_frame, text='Output Path:', background=BACKGROUND_COLOR)
    output_path_label.grid(row=1, column=0, padx=5, pady=20)
    output_path = tkinter.Entry(file_frame, width=50)
    output_path.grid(row=1, column=1, pady=20, columnspan=40)
    output_folder_button = Button(file_frame,image = folder_photo, command = partial(getPath,'output'))
    output_folder_button.grid(row = 1, column=41,padx=10,pady=20)

    model_path_label = tkinter.Label(file_frame, text='Model Path:', background=BACKGROUND_COLOR)
    model_path_label.grid(row=2, column=0, padx=5, pady=20)
    model_path = tkinter.Entry(file_frame, width=50)
    model_path.grid(row=2, column=1, pady=20, columnspan=40)
    model_folder_button = Button(file_frame,image = folder_photo, command = partial(getPath,'model'))
    model_folder_button.grid(row = 2, column=41,padx=10,pady=20)

    #create_folders()


    root.mainloop()