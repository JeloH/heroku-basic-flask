import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route("/predict")
def predict():
    a1 = int(request.args.get('vol_moving_avg'))
    a2 = int(request.args.get('adj_close_rolling_med'))
    y_pred = model.predict(np.array([[a2, a1]]))
    test1=str(y_pred)
    print(y_pred)
    return test1
if __name__ == '__main__':
    app.run(port=5000, debug=True)
