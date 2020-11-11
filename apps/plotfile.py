import os
import numpy as np
from werkzeug.utils import secure_filename
# import keras.backend.tensorflow_backend as tb
# tb._SYMBOLIC_SCOPE.value = True
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.xception import (
	Xception, preprocess_input, decode_predictions)
from tensorflow.keras.models import load_model
from flask import Flask, request, redirect, url_for, jsonify, render_template, abort

import matplotlib.pyplot as plt
from app import load_model, getfile, prepare_model

model = Xception(weights='imagenet', include_top=True)
load_model()
getfile(request)
def load_model():
    	# load the pre-trained Keras model
	global model
	model = Xception(weights='imagenet', include_top=True)
print('**Keras Model Loading**')
load_model()
print('**Keras Model Loaded**')



def getfile(request):
	# Setup file retrieve from post
	f = request.files['file']

	# Save the file to uploads folder
	basepath = os.path.dirname(__file__)
	file_path = os.path.join(
		basepath, 'Uploads', secure_filename(f.filename))
	f.save(file_path)
	return file_path


def prepare_model(image_path, model):
    	# resize the input image and preprocess it
    
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # predict
    predict = model.predict(x)
    # return the processed plot
    return predict
    
def imported_plots():
    # return the processed plot
    if request.method == 'POST':
        filesave2 = getfile(request)

        preds = prepare_model(filesave2, model)

        pclass = decode_predictions(preds, top=5)
        #test prediction
        result = str(pclass[0][2][1])

        # plot prediction
        a_one = str(pclass[0][0][1])
        a_two = str(pclass[0][1][1])
        a_three = str(pclass[0][2][1])
        a_four = str(pclass[0][3][1])
        one = str(pclass[0][0][2])
        two = str(pclass[0][1][2])
        three = str(pclass[0][2][2])
        four = str(pclass[0][3][2])

        animals = [a_one, a_two, a_three, a_four]
        probs = [one, two, three, four]
        print(probs)
        print(animals)
        # probs = "{:.3%}".format(str(probs))
        y = np.arange(len(animals))
        plt.bar(y, probs)
        plt.xticks(y, animals)

        
        test = plt.show()

        # x_axis = np.arange(len(animals))
        # plt.figure(figsize=(8.25,6))
        # plt.bar(x_axis, probs, color=['darkgreen', 'lightgreen', 'yellow','orange'], align="edge")
        # tick_locations = [value for value in x_axis]
        # plt.xticks(tick_locations, animals, rotation=45, fontsize=15)
        # for index, value in enumerate(probs):
        #     plt.text(index + .15, value + .05, str('{:.3f}%'.format(value*100)), color='black', fontweight='bold', rotation=10, fontsize=12)
        # plt.title("Probabilities of Dog Breed", fontsize=15, fontweight='bold')
        # plt.xlabel("Dog Breeds", fontsize=15, fontweight='bold')
        # plt.ylabel("Probabilities", fontsize=15, fontweight='bold')
        # plt.xlim(-.5, len(x_axis)+.25)
        # plt.ylim(0, max(probs)+.515)
        # test = plt.show()
        return test
    return None