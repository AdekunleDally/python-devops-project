from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/timestamp', methods=['GET'])
def get_timestamp():
  import time
  ts =time.time()
 
  return jsonify({'timestamp':ts})

if __name__== '__main__':
  app.run(debug=True)
