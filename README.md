## Introduction

This is a Flask web service that is used for predicting the house price of unit area, given the house features ( "**_transaction date,  house age, distance to the nearest MRT station, number of convenience stores, latitude and longitude_**").

## Model behind

We used Sickit Learn to train a model using the Linear Regression algorithm, and in the service, we just use the parameters(**_thetas_**) we've got from the algorithm.

## How to use

- send a POST request to the service containing the house features
- example of the data to pass:
    - { "transaction_date" : "2012.917" 
        , "house_age" : "32" 
        , "nearest_distance" : "84.87882"
        , "num_convenience_stores" : "10" 
        , "latitude" : "24.98298" 
        , "longitude" : "121.54024" }

