import os
import numpy as np
from werkzeug.utils import secure_filename
import keras
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.xception import (
    Xception, preprocess_input, decode_predictions)
import tensorflow as tf
from flask import Flask, request, redirect, url_for, jsonify, render_template, abort
import glob
import pandas as pd 
#Start Flask 
app = Flask(__name__, template_folder='template')

app.config['upload_Folder'] = 'D:/Trilogy/Homework/final-project/dogImages/test/*'

#setup pretrained Xception model
model = Xception(weights='imagenet', include_top=True)
print('Model Loaded')
#setup file read from local
def local_files():
    file_glob = list(sorted(glob.glob('dogImages/test/*.jpg')))[-20:]
    pred_list = []
    for img_path in file_glob:
        img = image.load_img(file_glob, target_size=(299,299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        #prediction load
        prediction_3 = model.predict(x)

        #decode tuples in to list w/ predict %
        prediction_outcome = decode_predictions(prediction_3, top=3)
        pred_list.append(prediction_outcome)
    return pred_list


#setup file upload function
def file_import(request):
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    return file_path

#set main page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



#setup Xception path func
@app.route('/', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':    
    #import workaround to avoid thread error
        import keras.backend.tensorflow_backend as tb
        tb._SYMBOLIC_SCOPE.value = True

        #build ML params
        file_glob = list(sorted(glob.glob('Uploads/*.jpg')))[-20:]
        file_path = file_import(request)
        #xception image preprocess
        img = image.load_img(file_path, target_size=(299,299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        #prediction load
        prediction = model.predict(x)

        #decode tuples in to list w/ predict %
        prediction_outcome = decode_predictions(prediction, top=4)

        return render_template('index.html', prediction = prediction_outcome, labels = file_glob)

if __name__ == "__main__":
    app.run(debug=True)