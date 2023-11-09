import tensorflow as tf
from PIL import Image
import numpy as np
from skimage import transform


IMG_SIZE = (224, 224, 3)



class makePrediction:
    def __init__(self,model_path):
        try:
            self.model = tf.keras.models.load_model(model_path)
        except Exception as e:
            print(e)
    def load_image(self,filename):
        np_image = Image.open(filename)
        np_image = np.array(np_image).astype('float32') #had to remove /255.
        np_image = transform.resize(np_image, IMG_SIZE)
        np_image = np.expand_dims(np_image, axis=0)
        return np_image

    def make_predict(self,filename):
        image = self.load_image(filename)
        return np.rint(self.model.predict(image)[0][0])




if __name__ == "__main__":
    import random
    import os
    predict = makePrediction(r"cnn_model")
    path = r"input//"
    for i in range(30):
        random_image = f"{path}{random.choice(os.listdir(path))}"
        print(predict.make_predict(random_image))