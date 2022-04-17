from flask import Flask, render_template, request
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import requests
import json 
import html
import os



app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def predict():
    imagefile = request.files["imagefile"]
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    
    r = requests.post(
    "https://api.deepai.org/api/deepdream",
    files={
        'image': open(str(image_path), 'rb'),
    },

    headers={'api-key': '35967d55-2dbd-48b5-b178-70049c2c62d0'}
    )

    jsonfile = r.json()

    jsonfile = jsonfile["output_url"]
    stripped_string = jsonfile.strip("")

    return render_template('index.html', title="page", answer = str(stripped_string) )

@app.route("/ai")
def about():
    return render_template("ai.html")


@app.route("/NeuralNetworks")
def neuralnetwork():
    return render_template("neural.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)