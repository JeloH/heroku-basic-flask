import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

y_pred = model.predict(np.array([[3.14371429e+05, 2.03099995e+01]]))

@app.route("/predict")
def predict():
    vol_moving_avg = request.args.get('vol_moving_avg')
    adj_close_rolling_med = request.args.get('adj_close_rolling_med')
    test1=str(y_pred)
    print(y_pred)
    return test1
if __name__ == '__main__':
    app.run(port=5000, debug=True)
