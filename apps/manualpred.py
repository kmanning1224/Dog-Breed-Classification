import os
import numpy as np
from werkzeug.utils import secure_filename 
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

def load_model():
    	# load the pre-trained Keras model
	global model
	model = Xception(weights='imagenet', include_top=True)
print('**Keras Model Loading**')
load_model()

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



def predict1():
    """Use Xception to label image"""
    path = 'static/Images/american-bulldog.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict2():
    """Use Xception to label image"""
    path = 'static/Images/basset-hound.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict3():
    """Use Xception to label image"""
    path = 'static/Images/beagle.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result
def predict4():
    """Use Xception to label image"""
    path = 'static/Images/boxer.jpeg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict5():
    """Use Xception to label image"""
    path = 'static/Images/cavalier.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict6():
    """Use Xception to label image"""
    path = 'static/Images/chihuahua.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict7():
    """Use Xception to label image"""
    path = 'static/Images/chinese-crested.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict8():
    """Use Xception to label image"""
    path = 'static/Images/chow-chow.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict9():
    """Use Xception to label image"""
    path = 'static/Images/corgi.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result


def predict10():
    """Use Xception to label image"""
    path = 'static/Images/dachshund.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict11():
    """Use Xception to label image"""
    path = 'static/Images/german-shepherd.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result

def predict12():
    """Use Xception to label image"""
    path = 'static/Images/great-dane.jpg'
    
    img = image.load_img(path,target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pclass = decode_predictions(preds, top=5)
    result = str(pclass[0][0][1])
    bad_chars=[';',':','_','!','*']
    for i in bad_chars:
        result = result.replace(i, ' ')
        result = result.title()
            
        print(result)
    return result