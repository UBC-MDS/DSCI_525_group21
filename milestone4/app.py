from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# 1. Load your model here
model = joblib.load("model.joblib")

# 2. Define a prediction function
def return_prediction(X_predict):    
    return model.predict(X_predict)

# 3. Set up home page using basic html
@app.route("/")
def index():
    # feel free to customize this if you like
    return """
    <h1>Welcome to our rain prediction service</h1>
    To use this service, make a JSON post request to the /predict url with 5 climate model outputs.
    """

# 4. define a new route which will accept POST requests and return model predictions
@app.route('/predict', methods=['POST'])
def rainfall_prediction():
    content = request.json  # this extracts the JSON content we sent

    #print(type(content))
    
    X_predict = pd.DataFrame(content)
    
    prediction = return_prediction(X_predict)
    #print(prediction)

    results =  {'predictions': prediction.tolist()}

    for col in X_predict.columns.tolist():
        results['input_' + col] = X_predict[col].values.tolist()

    return jsonify(results)