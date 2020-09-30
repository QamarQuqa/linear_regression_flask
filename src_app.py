from flask import Flask, render_template, request
import pandas as pd
import json

parameters = None
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_house_price():

    if request.method == 'POST':

        # import the predicting module

        import linear_model

        # get the data from the POST request

        house_features = request.get_json()

        # call the predicting function and return the result

        return linear_model.predict(house_features, parameters)
    else:

        return render_template('index.html')

if __name__ == '__main__':

    # read the parameters(thetas and theta0) from json file

    with open('lm_parameters.json', 'r') as parameters_file:
        parameters = json.loads(parameters_file.read())

    app.run(debug=True, use_reloader=True)
