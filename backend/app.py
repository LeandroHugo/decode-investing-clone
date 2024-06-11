from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Placeholder for prediction logic
    prediction = {"stock": data['stock'], "prediction": "Buy"}
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
