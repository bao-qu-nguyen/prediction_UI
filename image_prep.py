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

pre_image_path = r"Z:\Alex P\Bao\All Data\fail\\"
post_image_path = r"Z:\Alex P\Bao\\Fail_11_02_Trimmed\\"




def lmis_image_trim(file_path,file,post_image_path,prefix):
    image = img_as_float(io.imread(file_path))
    new_file = str(int(''.join(filter(str.isdigit, file)))) + "_" +prefix+ ".png"
    image_trimmed = img_as_float(image[:450,:])
    image_path = post_image_path
    #plt.imsave(image_path + new_file, image_trimmed / 255.0, cmap='gray')
    return image_trimmed



################ Actual Loop #######################
for root, dirs, files in os.walk(pre_image_path):
    # select file name
    for file in files:
        file_path = os.path.join(root, file)
        try:
            lmis_image_trim(file_path,file,post_image_path,"fail")
        except:
            print("sumthang")