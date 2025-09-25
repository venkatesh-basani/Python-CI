from flask import Flask, jsonify
import os

app = Flask(__name__)

# Get the version from an environment variable.
# We'll use this to differentiate between v1 and v2.
APP_VERSION = os.environ.get("APP_VERSION", "unknown")

@app.route('/')
def hello_world():
    return jsonify(message=f"Hello, this is {APP_VERSION} of the application")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
