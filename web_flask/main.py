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

@app.route('/resgister')
def resgister():
    return render_template('create_account.html',
                           title="EatsExpress - Resgister")

@app.route('/cart')
def cart():
    return render_template('viewcart.html',
                           title="EatsExpress - cart")

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html',
                           title="EatsExpress - Restaurant")

@app.route('/home')
def home2():
    return render_template('main_loggedin.html',
                           title="EatsExpress - Home")

@app.route('/search')
def search():
    return render_template('filter.html',
                           title="EatsExpress - Search")

@app.route('/item')
def item():
    return render_template('add_item_to_cart.html',
                           title="EatsExpress - item")

@app.route('/addaddress')
def addaddress():
    return render_template('add_address.html',
                           title="EatsExpress - add address")

@app.route('/addaddress')
def addaddress():
    return render_template('add_address.html',
                           title="EatsExpress - add address")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
