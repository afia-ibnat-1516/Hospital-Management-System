from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file
db = SQLAlchemy(app)

# Define your models in models.py (e.g., User model)
# from models import User

if __name__ == '__main__':
    app.run(debug=True)
