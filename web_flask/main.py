from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html',
                           title="EatsExpress - Home")

@app.route('/login')
def login():
    return render_template('login.html',
                           title="EatsExpress - Login")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
