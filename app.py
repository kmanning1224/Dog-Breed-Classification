import os
import numpy as np
from werkzeug.utils import secure_filename 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import (
	Xception, preprocess_input, decode_predictions)
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template
import glob
import pandas as pd
import json
from apps.manualpred import predict1, predict2, predict3, predict4, predict5, predict6,predict7, predict8, predict9, predict10, predict11, predict12

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
app = Flask(__name__, template_folder='template')


def load_model():
	# load the pre-trained Keras model
	global model
	model = Xception(weights='imagenet', include_top=True)
print('**Keras Model Loading**')
load_model()
print('**KERAS MODEL LOADED**')


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

@app.route('/prediction', methods=['GET','POST'])
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
    return jsons

@app.route('/plotmanual')
def create_plot2():
    img = ''
    preds = prepare_model(img, model)

    pclass = decode_predictions(preds, top=4)
    #test prediction
    

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
    return jsons

@app.route('/manualpreds1', methods=['POST'])
def manualpred1():
    pred = predict1()
    print(pred)
    return pred		

@app.route('/manualpreds2', methods=['POST'])
def manualpred2():
    pred = predict2()
    print(pred)
    return pred

@app.route('/manualpreds3', methods=['POST'])
def manualpred3():
    pred = predict3()
    print(pred)
    return pred	

@app.route('/manualpreds4', methods=['POST'])
def manualpred4():
    pred = predict4()
    print(pred)
    return pred

@app.route('/manualpreds5', methods=['POST'])
def manualpred5():
    pred = predict5()
    print(pred)
    return pred

@app.route('/manualpreds6', methods=['POST'])
def manualpred6():
    pred = predict6()
    print(pred)
    return pred

@app.route('/manualpreds7', methods=['POST'])
def manualpred7():
    pred = predict7()
    print(pred)
    return pred

@app.route('/manualpreds8', methods=['POST'])
def manualpred8():
    pred = predict8()
    print(pred)
    return pred

@app.route('/manualpreds9', methods=['POST'])
def manualpred9():
    pred = predict9()
    print(pred)
    return pred

@app.route('/manualpreds10', methods=['POST'])
def manualpred():
    pred = predict10()
    print(pred)
    return pred

@app.route('/manualpreds11', methods=['POST'])
def manualpred11():
    pred = predict11()
    print(pred)
    return pred

@app.route('/manualpreds12', methods=['POST'])
def manualpred12():
    pred = predict12()
    print(pred)
    return pred

@app.route('/about')
def aboutproject():
    return render_template("about.html")

@app.route('/adopt')
def adopt():
    return render_template("adopt.html")


if __name__ == "__main__":
	app.run(debug=True)
