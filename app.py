# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Route to display the list of books
@app.route('/books')
def books():
    # Query all books from the database
    all_books = Book.query.all()
    
    # Render the HTML template with the list of books
    return render_template('books.html', books=all_books)

# Route to add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get the form data for the new book
        title = request.form['title']
        author = request.form['author']
        pub_year = request.form['pub_year']

        # Create a new Book object
        new_book = Book(title=title, author=author, pub_year=pub_year)
        
        # Add the new book to the database session
        db.session.add(new_book)
        
        # Commit the changes to the database
        db.session.commit()

        # Redirect to the '/books' route after adding the book
        return redirect(url_for('books'))

    # Render the HTML template for adding a new book
    return render_template('add_book.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
