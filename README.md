## Introduction

This is a Flask web service that is used for predicting the house price of unit area, given the house features ( "**_transaction date, house age, distance to the nearest MRT station, number of convenience stores, latitude and longitude_**").

## Model behind

We used Sickit Learn to train a model using the Linear Regression algorithm, and store the model into Pickel file. In the service, we read the model from the Pickel file then use it to make predictions.

## How to use

#### to build the docker image:

- run the command `docker build -t linear_model`
  - the `-t` is used to set the a TAG for the docker image

#### to run the service without the docker:

- run the command `python3 src_app.py -path pickle_file_path`
  - the `pickle_file_path` is the entire path of the pickle file which is stored in the service directory

#### to use the service:

- send a POST or GET request to the service containing the house features
- example of the passed data:
  - { "transaction_date" : "2012.917"
    , "house_age" : "32"
    , "nearest_distance" : "84.87882"
    , "num_convenience_stores" : "10"
    , "latitude" : "24.98298"
    , "longitude" : "121.54024" }
