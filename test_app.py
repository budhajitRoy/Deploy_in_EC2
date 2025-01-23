
# import the flask app we defined in the app.py file
from app import app 

# import pytest
import pytest 


# define the way we can mimic the api call
# the below code will create a kind of a dummy server and mimic the api call so that we can test the flask app

@pytest.fixture   ## this decorator is required, just need to remember this syntax when testing flask app using pytest
def client():
    return app.test_client()


# test the ping end-point
def test_ping(client):
    resp = client.get("/ping") # get the response
    assert resp.text == "Hello, World!"
    # in the above, the resp will get the status code value like [200 OK]
    # in order to get the response as text, we need to specify as resp.text


# test the predict_churn end-point
def test_predict(client):

    # set up test data
    test_data = {
        "Day Mins" : -1.3074965, 
        "Eve Mins" :  0.08947901, 
        "Night Mins" : 0.39653914,
        "CustServ Calls" : -0.54879454,
        "Account Length" : -0.61621064
    }


    resp = client.get("/predict_churn", json = test_data)
    assert resp.text in ["Churn", "Not Churn"] # test if the predicted response is either Churn or Not Churn
    assert resp.text == "Not Churn" # test if the predicted response is Churn

# to test, we just need to run as :pytest test_app.py, it will run all test in this test_app.py file
# if we run only as pytest, it will search for all files with name test_ in this folder and run it
