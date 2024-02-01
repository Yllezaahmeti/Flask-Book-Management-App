# Flask Book Management App

This is a simple Flask web application for managing a list of books. Users can view a list of books and add new books using a web interface.

## Features

- View a list of books with their titles, authors, and publication years.
- Add new books using a simple form.

## Project Structure

- `app.py`: Main Flask application file.
- `init_app.py`: Script for initializing the database and adding dummy data.
- `models.py`: Defines the Book model using Flask-SQLAlchemy.
- `templates/`: Contains HTML templates for rendering pages.
- `static/`: Contains CSS stylesheets.

## Setup

1. Install dependencies:

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

2. Run the initialization script to create the database and add dummy data:

    ```bash
    python init_app.py
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

Visit `http://127.0.0.1:5000/` in your web browser to access the application.

## Usage

- Visit `/books` to view the list of books.
- Visit `/add_book` to add a new book using the form.


