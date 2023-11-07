import tkinter
from tkinter import*
from PIL import Image, ImageTk
import tensorflow as tf
import shutil
from config import *
import os
from image_prep import*
import numpy as np
from matplotlib import cm
from skimage import data
import cv2


BACKGROUND_COLOR = "#EBE8E2"

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
        os.mkdir(OUTPUT_FOLDER)
        for path in PATHES:
            os.mkdir(path)




def convertToPNG(path):
    img_path = path
    img_file = cv2.imread(img_path)  # read in the image with OpenCV
    img_file = np.uint8(img_file)  # convert image into an unsigned 8 bit int array with NumPy
    img_file = Image.fromarray(img_file)  # read in image from array with Tkinter
    img_file = img_file.resize((IMG_H, IMG_W))
    return img_file




if __name__ == '__main__':
    root = Tk()
    root.title('LMIS Image Classification')
    root.config(padx=20,pady=20, background= BACKGROUND_COLOR)



    frame = tkinter.Frame(root,background=BACKGROUND_COLOR)
    frame.pack()

    image_frame = tkinter.LabelFrame(frame,background= BACKGROUND_COLOR)
    image_frame.grid(row = 0,column = 0)

    file_path = r"C:\Users\darkm\OneDrive\Desktop\LMIS_CNN\Predict_UI\images\2a.tif"
    img_file = convertToPNG(file_path)
    create_img = ImageTk.PhotoImage(img_file)
    image = Label(image_frame, image = create_img)
    image.grid(row = 0 ,column=0,padx=20,pady=20)

    button_frame = tkinter.LabelFrame(frame,background=BACKGROUND_COLOR)
    button_frame.grid(row=1,column = 0,padx=50,pady=50)
    predict_btn = Button(button_frame, text = "Run Prediction")
    predict_btn.grid(row = 0 ,column=0,rowspan= 2,columnspan=2, padx=20,pady=20)

    file_frame= tkinter.LabelFrame(frame,background=BACKGROUND_COLOR)
    file_frame.grid(row =0,column=1,padx= 50,pady=50)

    folder_photo = PhotoImage(file = r"images\folder_icon.png").subsample(100,100)

    input_path = tkinter.Entry(file_frame,width=50)
    input_path.grid(row = 0,column = 0,padx=20,pady=20, columnspan=40)
    input_folder_button = Button(file_frame,image = folder_photo)
    input_folder_button.grid(row = 0, column=40,padx=10,pady=20)


    output_path = tkinter.Entry(file_frame, width=50)
    output_path.grid(row=1, column=0, pady=20, columnspan=40)

    create_folders()

    root.mainloop()