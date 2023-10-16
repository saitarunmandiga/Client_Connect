from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer_data')
def customer_data():
    return render_template('customer_data.html')

@app.route('/input_data')
def input_data():
    return render_template('input_data.html')

@app.route('/search_data')
def search_data():
    return render_template('search_data.html')

if __name__ == '__main__':
    app.run(debug=True)

