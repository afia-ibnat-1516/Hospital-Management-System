import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list to store nutrition records (you should replace this with a database)
nutrition = []

@app.route('/')
def nutrition():
    return render_template('nutrition.html')

@app.route('/add_record', methods=['POST'])
def add_record():
    food_item = request.form['food_item']
    calories = request.form['calories']
    date = request.form['date']
    
    record = {'food_item': food_item, 'calories': calories, 'date': date}
    nutrition.append(record)
    
    return redirect(url_for('nutrition'))

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html', nutrition=nutrition)

if __name__ == '__main__':
    app.run(debug=True)
