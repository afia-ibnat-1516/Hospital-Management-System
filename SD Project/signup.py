from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(_name_)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Here you would typically add the user to the database
        # For now, we'll just simulate a successful signup
        flash('Account created successfully!', 'success')
        return redirect(url_for('signup'))
    
    return render_template('signup.html')

if _name_ == '_main_':
    app.run(debug=True)