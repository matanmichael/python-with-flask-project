from flask import Flask, render_template, request, redirect, url_for, flash
from tools.books import Book
from tools.customers import Customer
from tools.loans import Loan 

book_instance=Book()
customer_instance=Customer()
loan_instance=Loan()
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addbook', methods=['GET', 'POST'])
def addBook():
    if request.method == 'POST':
        book_instance.addNewBook()
        flash("Book added successfully", 'success')
        return redirect(url_for('addBook'))  # Redirect to the add book page after adding
    return render_template('addbook.html')

@app.route('/books', methods=['GET'])
def displayBooks():
    all_books = book_instance.DisplayAllBooks()
    return render_template("displaybooks.html", books=all_books)

@app.route('/removebook', methods=['POST'])
def removeBook():
    book_id = request.form.get('book_id')
    if book_id:
        result = book_instance.removeBook(book_id)
        if result:
            flash("Book removed successfully", 'success')
        else:
            flash("Book not found or could not be removed", 'danger')
    else:
        flash("Please provide a valid book ID", 'danger')

    return redirect(url_for('displayBooks'))
  
@app.route('/bookfinder', methods=['GET', 'POST'])
def search_books():
    found_books = []
    if request.method == 'POST':
        search_text = request.form['search_text']
        found_books = book_instance.bookFinder(search_text)
    return render_template('search_results.html', found_books=found_books)

# app.py
@app.route('/addcustomer', methods=['GET', 'POST'])
def addCustomer():
    if request.method == 'POST':
        customer_instance.addNewCustomer()
        flash("Customer added successfully", 'success')
        return redirect(url_for('addCustomer'))  # Redirect to the add customer page after adding
    return render_template('addcustomer.html')

@app.route('/customers', methods=['GET'])
def displayCustomers():
    all_customers = customer_instance.displayAllCustomers()
    return render_template("displaycustomers.html", customers=all_customers)

@app.route('/removecustomer', methods=['POST'])
def removeCustomer():
    customer_id = request.form.get('customer_id')
    if customer_id:
        result = customer_instance.removeCustomer(customer_id)
        if result:
            flash("Customer removed successfully", 'success')
        else:
            flash("Customer not found or could not be removed", 'danger')
    else:
        flash("Please provide a valid customer ID", 'danger')

    return redirect(url_for('displayCustomers'))

@app.route('/customerfinder', methods=['GET', 'POST'])
def search_customers():
    found_customers = []
    if request.method == 'POST':
        search_text = request.form['search_text']
        found_customers = customer_instance.customerFinder(search_text)
    return render_template('search_customer.html', found_customers=found_customers)

@app.route('/loans', methods=['GET'])
def displayLoans():
    all_loans = loan_instance.displayAllLoans()
    return render_template("displayloans.html", loans=all_loans)

@app.route('/addloan', methods=['GET', 'POST'])
def addLoan():
    if request.method == 'POST':
        loan_instance.loan_book()
        flash("Book added successfully", 'success')
        return redirect(url_for('addLoan'))  # Redirect to the add book page after adding
    return render_template('addloan.html')

@app.route('/removeloan', methods=['POST'])
def removeLoan():
    if request.method == 'POST':
        loan_instance.return_book()
    return redirect(url_for('displayLoans'))

@app.route('/lateloans', methods=['GET'])
def displayLateLoans():
    all_late_loans = loan_instance.display_late_loans()
    return render_template("displaylateloans.html", late_loans=all_late_loans)

if __name__ == '__main__':
    app.run(debug=True)
