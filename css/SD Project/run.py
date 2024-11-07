# run.py

from app import app, db
from app.models import User

if __name__ == '__main__':
    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
