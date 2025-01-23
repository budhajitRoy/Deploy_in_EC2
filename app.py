from flask import Flask, request

# this line creates a web server
app = Flask(__name__)

# this decorator will define the api end-point 
# by default a browser only a GET request
# and if methods are not explicitly, it is a GET method
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# to run : flask --app churn_app run

@app.route("/ping", methods = ['GET'])
def hello_world():
    return "Hello, World!"


## churn prediction 
import joblib

# get the models and the scaler object
churn_model = joblib.load("./churn_model.pkl")
# scaler = joblib.load("./scaler.pkl")

cols = ['Day Mins', 'Eve Mins', 'Night Mins', 'CustServ Calls', 'Account Length']
dummy_data = [-0.63371648,  0.279073  ,  0.02116186,  1.93631281, -0.38704416] # churn
dummy_data = [-1.3074965 ,  0.08947901,  0.39653914, -0.54879454, -0.61621064] # not churn

sample_data = {
    'Day Mins' : -1.3074965, 
    'Eve Mins' :  0.08947901, 
    'Night Mins' : 0.39653914,
    'CustServ Calls' : -0.54879454,
    'Account Length' : -0.61621064
}

# using hard coded data
# @app.route("/predict_churn")
# def predict():
#     prediction = churn_model.predict([test_data])

#     if prediction[0] == 1:
#         return "Churn"
#     else:
#         return "Not Churn"

# using input parameters passed in the request
@app.route("/predict_churn", methods=['GET']) # setting up method as POST
def predict():
    input_data = request.get_json()
    #  print(input_data)

    # getting only the values from the json input request
    test_data = list(input_data.values())

    prediction = churn_model.predict([test_data])

    if prediction[0] == 1:
        return "Churn"
    else:
        return "Not Churn"

## command to run : flask --app app run
