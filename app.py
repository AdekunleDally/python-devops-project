from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/timestamp', methods=['GET'])
def get_timestamp():
    ts = time.time()
    return jsonify({'timestamp': ts})

if __name__ == '__main__':
    app.run(debug=True)
