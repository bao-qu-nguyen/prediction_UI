import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import shutil
import os
from PIL import Image, ImageFilter, ImageOps
from scipy import ndimage as nd
from skimage import* # data, img_as_float
from skimage import io
from skimage.util import img_as_float
import cv2
from config import*
class ImagePreProcessing:
    def image_preprocess(self,image_path):
        img_file = cv2.imread(image_path)[:450, :]  # read in the image with OpenCV
        img_file = np.uint8(img_file)  # convert image into an unsigned 8 bit int array with NumPy
        img_file = Image.fromarray(img_file)  # read in image from array with Tkinter
        return img_file


    # def convertToPNG(image_path):
    #     img_file = cv2.imread(image_path)  # read in the image with OpenCV
    #     img_file = np.uint8(img_file)  # convert image into an unsigned 8 bit int array with NumPy
    #     img_file = Image.fromarray(img_file)  # read in image from array with Tkinter
    #     #img_file = img_file.resize((IMG_H, IMG_W))
    #     return img_file


#
# if __name__ =="__main__":
#     ################ Actual Loop #######################
#     for root, dirs, files in os.walk(pre_image_path):
#         # select file name
#         for file in files:
#             file_path = os.path.join(root, file)
#             try:
#                 lmis_image_trim(file_path,file,post_image_path,"fail")
#             except:
#                 print("sumthang")