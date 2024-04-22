from flask import Flask, jsonify, request
from get_directions import Conestoga, Fairway  # Import your module or function

app = Flask(__name__)

@app.route('/api/function', methods=['POST'])
def call_function():
    result = Conestoga()  # Call your function with data from the request
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)