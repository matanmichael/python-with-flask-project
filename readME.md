Book Library Management System.
This is a simple Python Flask application for managing a book library system with an SQLite database. The project includes a Data Access Layer (DAL), unit tests, and a web-based client application that interacts with the library system.

Prerequisites
Before running the application, make sure you have the following prerequisites installed on your system:

Python 3
Flask
SQLite

Installation

Clone the repository:
git clone [https://github.com/yourusername/book-library-management.git](https://github.com/matanmichael/python-with-flask-project.git)
cd python-with-flask-project.git

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Initialize the SQLite database:
flask init-db

Run the Flask application:
flask run

The application will be accessible at http://localhost:5000.

Database Structure
The SQLite database consists of three tables:

Books:

id (Primary Key)
name
author
year_published
type (1/2/3)
Customers:

id (Primary Key)
name
city
age
Loans:

cust_id (Foreign Key to Customers)
book_id (Foreign Key to Books)
loan_date
return_date
The book type determines the maximum loan time:

Type 1: Up to 10 days
Type 2: Up to 5 days
Type 3: Up to 2 days
Web Client Application
The web-based client application provides a user-friendly interface for library management. You can perform the following operations:

Add a new customer
Add a new book
Loan a book
Return a book
Display all books
Display all customers
Display all loans
Display late loans
Find a book by name
Find a customer by name
Remove a book
Remove a customer
Access the application in your web browser at http://localhost:5000.

Unit Tests
Unit tests are provided to ensure the correctness of the Data Access Layer and Flask routes. You can run the tests using the following command:
pytest

Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes. We welcome any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was created as a simple example of a book library management system using Python Flask and SQLite and is intended for educational purposes. Thank you to the open-source community for providing the tools and libraries used in this project.
