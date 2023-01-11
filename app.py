import re
from turtle import pos
from flask import send_file
from flask import Flask,request,jsonify
from flask_restful import Api,Resource
import os 
import soundfile
import numpy as np
import librosa as lib
import requests
import werkzeug



app=Flask(__name__)
api=Api(app)


@app.route("/")
def Homepage():
 return "Escope"
            

@app.route("/predict", methods=["POST"])
def fft():
 if request.method == "POST" :
            data=request.get_json()
            filename=data['name']
            URL=data['url'] 
            print(filename)
            print("before downloading")
            response = requests.get(str(URL))
            print("downloaded")
            filename=filename+".wav"
            open("audio_testdata/"+filename, "wb").write(response.content)
            print(filename)
            return filename
    

    


@app.route("/helloworld", methods=["POST"])
def Helloworld():
    
    return "Hello world"
        
if __name__=="__main__"  :
    app.run()  