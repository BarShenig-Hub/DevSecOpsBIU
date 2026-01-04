from flask import Flask
from flask import request
from flask import render_template_string, redirect, url_for, jsonify

CREDENTIALS = ('admin', 'Aa123456')

user1 = {'name': 'James', 'ID': 12345678}
user2 = {'name': 'Diana', 'ID': 87654321}
users = {101: user1, 102: user2}


app = Flask(__name__)

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign in</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            font-family: "Segoe UI", Arial, sans-serif;
            background: linear-gradient(135deg, #0a3d62, #1e90ff);
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-box {
            background: #f5f6fa;
            padding: 30px;
            width: 320px;
            border-radius: 6px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }
        h2 {
            text-align: center;
            font-weight: 400;
            color: #2f3640;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            margin-top: 20px;
            padding: 10px;
            background: #0078d4;
            border: none;
            color: white;
            font-size: 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #005a9e;
        }
        .error {
            color: red;
            margin-top: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Sign in</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign in</button>
        </form>
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if (username, password) == CREDENTIALS:
            return redirect(url_for("get_users"))
        else:
            return render_template_string(LOGIN_HTML, error="Invalid credentials")

    return render_template_string(LOGIN_HTML)


@app.route("/users", methods=["GET"])
def get_users():
    return users



@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/users', methods=['GET'])
def get_all_users():
    return users

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    user_id = max(users.keys()) + 1
    users[user_id] = new_user
    return users

# curl -X POST -H "Content-Type: application/json" -d '{"name": "Daniel", "ID": 45123678}' http://localhost:5000/users

@app.route('/users', methods=['PUT'])
def update_user_id():
    data = request.get_json()

    name = data.get('name')
    new_id = data.get('ID')

    for user in users.values():
        if user['name'] == name:
            user['ID'] = new_id

    return users

# curl -X PUT -H "Content-Type: application/json" -d '{"name": "Diana", "ID": 8860936}' http://localhost:5000/users


@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.get_json()

    name = data.get('name')

    for user_key, user in list(users.items()):
        if user['name'] == name:
            del users[user_key]

    return users

# url -X DELETE -H "Content-Type: application/json" -d '{"name": "Diana"}' http://localhost:5000/users


app.run()