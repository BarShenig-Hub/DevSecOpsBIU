from flask import Flask, jsonify, request
import requests
from flask import render_template_string, redirect, url_for, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if (username, password) == ('admin', 'Aa123456'):
            return get_external_data()
        else:
            return "Invalid credentials"

    return 'Type username and password with curl command'

# curl -H "Content-Type: application/json" -d '{"username":"admin","password":"Aa123456"}' -L http://localhost:5000
# to show the data after login in the linux shell

@app.route('/breeds')
def get_external_data():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    data = response.json()
    return jsonify(data)

@app.route('/breeds/filtered/<breed_name>', methods=["GET"])
def get_filtered_data(breed_name):
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    data = response.json()
    all_breeds = data.get('message', {})
    if breed_name in all_breeds:
        return jsonify({
            "breed": breed_name,
            "sub_breeds": all_breeds[breed_name]
        })
    else:
        return jsonify({"error": "Breed not found"}), 404


app.run()
