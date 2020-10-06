from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import json
import argparse
import os
from sklearn.linear_model import LinearRegression
import pickle
import config

linear_regression_model = None
app = Flask(__name__)


def read_arguments():
    """reads the pickle file path from the console

    Returns:
        string: the pickle file path which contains the linear regression model
    """
    # set a usage to show how to run the service
    usage = '%(prog)s [-h] --model_path'

    # set a description about this service
    description = "This is a Flask web service that is used for predicting the " + \
        "house price of unit area"

    # create the parser and set the usage and the description
    parser = argparse.ArgumentParser(description=description, usage=usage)

    # define an argument to be passed to parse and get it
    parser.add_argument('-path', dest='model_path', type=str, required=True,
                        help='the pickle file path')

    # get the argument which is the model file path
    args = parser.parse_args()

    # return the model file path
    return args.model_path


def read_linear_regression_model(pickle_file_path):
    """read the model form the path passed in arguments

    Args:
        pickle_file_path (string): the pickle file path

    Returns:
        sklearn.linear_model._base.LinearRegression: the linear regression model
    """
    # read the linear regression model from the pickle file
    linear_regression_model = pickle.load(open(pickle_file_path, 'rb'))

    # return the model
    return linear_regression_model


def predict(linear_regression_model, house_features):
    """predinc the house price using the linear regression model for the house
       features

    Args:
        linear_regression_model ( sklearn.linear_model._base.LinearRegression):
            the linear regression model
        house_features (dict): the house features to predict for

    Returns:
        dict: the predict value stored in dict
    """

    # slice the features values
    features_values = [float(house_features.get(
        feature)) for feature in config.FEATURES_NAMES_IN_ORDER]

    # create a numpy array of the features values and reshape it into 2D,
    # due to he predict function assumes a 2D array where each line is a
    # sample to predict for
    features_values_in_shape = np.array(features_values).reshape(1, 6)

    # make the prediction
    predicted_house_price = linear_regression_model.predict(
        features_values_in_shape)

    # slice the predicted value
    json_reslut = {config.PREDICTED_VALUE: predicted_house_price[0]}

    # return the predicted value
    return json_reslut


@app.route('/')
def welcoming():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_house_price():

    # if the method is POST
    if request.method == 'POST':

        # get the data from the POST request
        house_features = request.get_json()

        # call the predicting function and return the result
        return json.dumps(predict(linear_regression_model, house_features))

    # if the method is GET
    else:

        # get the house_features from the get request
        house_features = {
            feature: request.args.get(feature)
            for feature in config.FEATURES_NAMES_IN_ORDER
        }

        # call the predicting function and return the result
        return json.dumps(predict(linear_regression_model, house_features))


if __name__ == '__main__':

    # get the model file path from the console
    pickle_file_path = read_arguments()

    # check if the file exists or not
    if not os.path.isfile(pickle_file_path):

        # display an error
        print("Error. Please make sure the file is existed!")

    else:

        # read the linear regression model
        linear_regression_model = read_linear_regression_model(
            pickle_file_path)

        # run the service
        app.run(host="0.0.0.0", port=8000)
