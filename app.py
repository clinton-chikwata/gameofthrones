from flask import Flask, render_template
import tablib
import os

app = Flask(__name__)     #checks to see if this module was called interactively and then calls the specified function to execute the code.
dataset = tablib.Dataset() #instantiate tablib object
with open(os.path.join(os.path.dirname(__file__), 'characters.csv')) as f: #reading data from csv file

    dataset.csv = f.read()                                                   #passing data to the tablib object


dataset1 = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__), 'episode_per_season.csv')) as f1:
    dataset1.csv = f1.read()

@app.route('/characters')           #specifying route used to access that resource
def index():
    data = dataset.html
    # return dataset.html
    return render_template('index.html', data=data)

@app.route("/episodes")
def characters():
    data = dataset1.html
    # return dataset.html
    return render_template('index.html', data=data)  #passing data from controller to views in templates folder 


if __name__ == "__main__":
    app.run(debug="true", port=80)