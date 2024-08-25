from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import time

app = Flask(__name__)

#setup prometheus metrics
metrics=PrometheusMetrics(app)
print("Prometheus metrics initialized")

@app.route('/', methods=['GET'])
def get_timestamp():
    ts = time.time()
    return jsonify({'timestamp': ts})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)