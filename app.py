import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/predict")
def predict():
    vol_moving_avg = request.args.get('vol_moving_avg')
    print(vol_moving_avg)
    adj_close_rolling_med = request.args.get('adj_close_rolling_med')
    print(adj_close_rolling_med)
    adj_close_rolling_med=3.14
    features = [np.array([vol_moving_avg, adj_close_rolling_med])]
    y_pred = model.predict(features)
    test1=str(y_pred)
    print(y_pred)
    return test1
if __name__ == '__main__':
    app.run(port=5000, debug=True)
