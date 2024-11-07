from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for handling sign-up submissions
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Process the data (you may want to store it in a database or perform other actions)
        # For this example, just print the data
        print(f"Received sign-up data - Name: {name}, Email: {email}, Password: {password}")

        # You can redirect the user to another page after sign-up
        return render_template('signup_success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
