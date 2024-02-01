# init_app.py
from flask import Flask
from models import db, Book

# Function to create and configure the Flask application
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

# Function to initialize the database by creating tables
def init_db(app):
    with app.app_context():
        db.create_all()

# Function to add dummy data to the database
def add_dummy_data():
    with app.app_context():
        # Create Book objects with dummy data
        book1 = Book(title='Book 1', author='Author 1', pub_year=2020)
        book2 = Book(title='Book 2', author='Author 2', pub_year=2021)
        
        # Add the books to the database session
        db.session.add(book1)
        db.session.add(book2)
        
        # Commit the changes to the database
        db.session.commit()

# Run the script if executed directly
if __name__ == '__main__':
    # Create the Flask application
    app = create_app()
    
    # Initialize the database
    init_db(app)
    
    # Add dummy data to the database
    add_dummy_data()
