from flask import Flask, jsonify
from flask.globals import request
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/ping', methods=["POST"])
def ping_endpoint():

    """Makes call to given url

    Returns:
        (dict): Response from the given url/endpoint
    """

    payload = request.json
    res = requests.get(payload["url"])
    res_js = res.json()
    return jsonify(res_js)


@app.route('/info', methods=["GET"])
def info_endpoint():

    """Simple API which gives info of organization

    Returns:
        (dict): Information
    """

    res = {"Receiver": "Cisco is the best!"}
    return res


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=3000)
