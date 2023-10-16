from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data storage (you can replace this with a database)
customer_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input_customer():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        contact_info = request.form['contact_info']
        # Save the data (you can add validation and error handling)
        customer_data.append({'name': customer_name, 'contact': contact_info})
        return redirect(url_for('input_customer'))  # Redirect to clear the form
    return render_template('input.html')

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve_customer():
    if request.method == 'POST':
        search_term = request.form['search_term']
        # Search for customer data (you can implement search logic here)
        results = [customer for customer in customer_data if search_term.lower() in customer['name'].lower()]
        return render_template('retrieve.html', results=results)
    return render_template('retrieve.html')

if __name__ == '__main__':
    app.run(debug=True)
