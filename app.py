from flask import Flask, request, Response, render_template

app = Flask(__name__)

# 🔐 Step 1: Define username and password
USERNAME = 'Valli'
PASSWORD = 'Yuvashree@2003'

# 🔐 Step 2: Authentication functions
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Could not verify your access. Login required.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

# 🔐 Step 3: Protect all routes
@app.before_request
def require_auth():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

# 🏠 Example route (replace with your own)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
