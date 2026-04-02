from flask import Flask, render_template, request

app = Flask(__name__)

# temporary user storage
users = {}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    users[username] = password

    return f"User {username} created successfully 😌✨"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f"Welcome {username} 🔥"
    else:
        return "Invalid details ❌"

app.run()