import joblib
import numpy as np
from flask import Flask, request, jsonify

# Load the model
model_path = "model.joblib"
model = joblib.load(model_path)

# Create a Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get the JSON data from the request
    data = request.json

    # Convert the data to a NumPy array
    input_data = np.array(data["data"])

    # Make predictions using the loaded model
    predictions = model.predict(input_data)

    # Convert the predictions to a list and return a JSON response
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)

