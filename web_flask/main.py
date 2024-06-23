from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html',
                           title = "EatsExpress")

@app.route('/login')
def login():
    return render_template('login.html',
                           title = "Login - EatsExpress")

@app.route('/register')
def register():
    return render_template('register.html',
                           title = "Register -EatsExpress")

if __name__ == '__main__':
    app.run(debug=True, port=5001)