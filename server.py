from flask import Flask, render_template, request , jsonify
import time
import os

import main as search

app = Flask(__name__)
#general parameters
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
params = {"theta": 4, "frequency": (0, 1, 0.5, 0.8), "sigma": (1, 3), "n_slice": 2}

#Database Offline Indexing
@app.route('/offlineIndex')
def test():
    index(params)
    return "Done !!"

#Index route
@app.route('/')
def index():
    return render_template('main.html' )

@app.post('/upload')
def upload():
    #Saving the Uploaded image in the Upload folder
    file = request.files['image']
    print(file.filename)
    #imgs= sh.GetSimilarPic("static/pics/"+file.filename)
    imgs= search.Search_Fct(file.filename)
    results=list()
    RESULTS_LIST = list()
   
    RESULTS_LIST.append(
            {"image": "static/pics/"+file.filename, "score": str(file.filename)}
        )
    for name in imgs:
            RESULTS_LIST.append(
            {"image": "static/pics/"+name.image_name, "score": str(name.image_name)}
        )

    #returning the search results 
    return jsonify(RESULTS_LIST)



app.run(debug=True)