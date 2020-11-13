import os
import numpy as np
from werkzeug.utils import secure_filename 
# import keras.backend.tensorflow_backend as tb
# tb._SYMBOLIC_SCOPE.value = True
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.xception import (
	Xception, preprocess_input, decode_predictions)
from tensorflow.keras.models import load_model
from flask import Flask, request, redirect, url_for, jsonify, render_template, abort, Response
import glob
import matplotlib.pyplot as plt
import pandas as pd
import json
# from apps.TEST import img_load_test as imgtst
# import python apps
# from apps.xception import prediction_local
# Start Flask
app = Flask(__name__, template_folder='template')


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

# def create_plot(filelocal):
#     print(filelocal)
    
#     preds = prepare_model(filelocal, model)

#     pclass = decode_predictions(preds, top=4)

#     # plot prediction
#     a_one = str(pclass[0][0][1])
#     a_two = str(pclass[0][1][1])
#     a_three = str(pclass[0][2][1])
#     a_four = str(pclass[0][3][1])
#     one = pclass[0][0][2]
#     two = pclass[0][1][2]
#     three = pclass[0][2][2]
#     four = pclass[0][3][2]
#     print(a_one, a_two, a_three, a_four)
#     animals = [a_one, a_two, a_three, a_four]
#     probs = [one, two, three, four]
#     print(type(pclass[0][0][2]))
#     x_axis = np.arange(len(animals))
#     print(x_axis)
#     plt.figure(figsize=(8.25,6))
#     plt.bar(x_axis, probs, color=['darkgreen', 'lightgreen', 'yellow','orange'], align="edge")
#     tick_locations = [value for value in x_axis]
#     plt.xticks(tick_locations, animals, rotation=45, fontsize=15)
    
    # for index, value in enumerate(probs):
    #     # p = value*100
    #     s = '{:.3f}%'.format(value*100)
    #     t = type(s)
    #     print(t)
    #     plt.text(index + .15, value + .05, s, color='black', fontweight='bold', rotation=10, fontsize=12)
    # plt.title("Probabilities of Dog Breed", fontsize=15, fontweight='bold')
    # plt.xlabel("Dog Breeds", fontsize=15, fontweight='bold')
    # plt.ylabel("Probabilities", fontsize=15, fontweight='bold')
    # plt.xlim(-.5, len(x_axis)+.25)
    # plt.ylim(0, max(probs)+.15)
    # plot = plt.show()
    # # plot = plt.savefig('./plots/plot.jpg')


    # return plot

def DataResult1():
    if request.method == 'POST':
        print(request)
        filesave2 = getfile(request)
        print(filesave2)
        preds = prepare_model(filesave2, model)

        pclass = decode_predictions(preds, top=5)
        #test prediction
        
        bad_chars=[';',':','_','!','*']
        result = str(pclass[0][0][1])

        for i in bad_chars:
            result = result.replace(i, ' ')
            result = result.title()
            
        print(result)
        # create_plot(filesave2)
        
        
        return result

def ImgResult():
    list_of_files = glob.glob('./uploads/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file



@app.route('/',  methods=['GET'])
def index():
    return render_template('final.html')

@app.route('/predictresult1', methods=['GET','POST'])
def result1():
    results = DataResult1()
    return results
    
@app.route('/plotfunc')
def create_plot():
    img = ImgResult()
    # print(img)
    preds = prepare_model(img, model)

    pclass = decode_predictions(preds, top=4)
    #test prediction
    
    bad_chars=[';',':','_','!','*']

    # plot prediction
    a_one = pclass[0][0][1]
    a_two = pclass[0][1][1]
    a_three = pclass[0][2][1]
    a_four = pclass[0][3][1]
    one = pclass[0][0][2]
    two = pclass[0][1][2]
    three = pclass[0][2][2]
    four = pclass[0][3][2]
    # print(a_one, a_two, a_three, a_four)
    animals = [a_one, a_two, a_three, a_four]
    probs = [one, two, three, four]
    dfs = pd.DataFrame({'Breed': animals,'Percentage': probs})
    jsons = dfs.to_json(orient="records")
    jsons = json.loads(jsons)
    jsons = json.dumps(jsons, indent=4)
    print(dfs)
    # test = df.to_json()
    # test = json.dumps(str(fulllib))
    # print(type(pclass[0][0][2]))
    # x_axis = np.arange(len(animals))
    # print(x_axis)
    # plt.figure(figsize=(8.25,6))
    # plt.bar(x_axis, probs, color=['darkgreen', 'lightgreen', 'yellow','orange'], align="edge")
    # tick_locations = [value for value in x_axis]
    # plt.xticks(tick_locations, animals, rotation=45, fontsize=15)
    
    # for index, value in enumerate(probs):
    #     # p = value*100
    #     s = '{:.3f}%'.format(value*100)
    #     t = type(s)
    #     print(t)
    #     plt.text(index + .15, value + .05, s, color='black', fontweight='bold', rotation=10, fontsize=12)
    # plt.title("Probabilities of Dog Breed", fontsize=15, fontweight='bold')
    # plt.xlabel("Dog Breeds", fontsize=15, fontweight='bold')
    # plt.ylabel("Probabilities", fontsize=15, fontweight='bold')
    # plt.xlim(-.5, len(x_axis)+.25)
    # plt.ylim(0, max(probs)+.15)
    # plot = plt.show()
    # plot = plt.savefig('./plots/plot.jpg')
    return jsons
			

if __name__ == "__main__":
	app.run(debug=True)
