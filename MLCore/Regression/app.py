from flask import Flask, request, jsonify,render_template

import pickle
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

## import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open("models/ridge.pkl","rb"))
standard_scaler=pickle.load(open("models/scaler.pkl","rb"))



@app.route("/")
def home():
    return render_tempalate("index.html")

from PythonBasics.Flask.flask import app


@app.route("/predictdata",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
        pass
    else:
        return render_template("home.html")
    


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
    