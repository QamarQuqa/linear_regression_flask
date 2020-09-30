import json

THETA0 = 'theta0'
PREDICTED_VALUE = 'predicted_value'


def predict(house_features, parameters):
    """
    predict the price of the house
    :params: the house features
    :params: the parameters (thetas)
    :return: the JSON file contains the predicted value
    """

    # the result predicted value

    predicted_value = float(parameters.get(THETA0))

    # calculate the predicted value by multiplying the feature and its theta

    for feature in house_features:
        predicted_value += float(house_features.get(feature)) \
            * float(parameters.get(feature))

    # the result in JSON to make more sense of the result

    json_reslut = {PREDICTED_VALUE : predicted_value}

    # return the predicted value

    return json.dumps(json_reslut)
