# models.py
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy extension
db = SQLAlchemy()

# Define the Book model representing the 'books' table in the database
class Book(db.Model):
    # Primary key column for the Book model
    id = db.Column(db.Integer, primary_key=True)
    
    # Title column with a maximum length of 50 characters, not nullable
    title = db.Column(db.String(50), nullable=False)
    
    # Author column with a maximum length of 50 characters, not nullable
    author = db.Column(db.String(50), nullable=False)
    
    # Publication year column, not nullable
    pub_year = db.Column(db.Integer, nullable=False)
