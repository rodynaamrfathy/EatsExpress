from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def EatsExpress():
    return render_template("/Users/rodynaamr/Desktop/EatsExpress/web_static/main.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)

