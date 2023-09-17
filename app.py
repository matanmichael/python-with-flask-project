from flask import Flask, render_template, request, flash, redirect, url_for
from tools.books import Book
from tools.customers import Customer
from tools.loans import Loan 

book_instance=Book()
customer_instance=Customer()
loan_instance=Loan()

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def displayBooks():
    all_books = book_instance.DisplayAllBooks()
    return render_template("displaybooks.html", books=all_books)

@app.route('/books/removebook', methods=['POST'])
def removeBook():
    book_id = request.form.get('book_id')
    book_instance.removeBook(book_id)
    flash("Book removed successfully", 'success')
    return render_template('displaybooks.html',books=book_instance.DisplayAllBooks())

@app.route('/books/addbook', methods=['GET', 'POST'])
def addBook():
    if request.method == 'POST':
        book_instance.addNewBook()
        flash("Book added successfully", 'success')       
    return render_template('addbook.html')

@app.route('/books/bookfinder', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        search_text = request.form['search_text']
        found_books = book_instance.bookFinder(search_text)
        return render_template('searchbook.html', found_books=found_books)
    return render_template('searchbook.html')

@app.route('/customers', methods=['GET'])
def displayCustomers():
    all_customers = customer_instance.displayAllCustomers()
    return render_template("displaycustomers.html", customers=all_customers)

@app.route('/removecustomer', methods=['POST'])
def removeCustomer():
    customer_id = request.form.get('customer_id')
    customer_instance.removeCustomer(customer_id)
    flash("Customer removed successfully",'success')
    return render_template('displaycustomers.html',customers=customer_instance.displayAllCustomers())

@app.route('/customers/addcustomer', methods=['GET', 'POST'])
def addCustomer():
    if request.method == 'POST':
        customer_instance.addNewCustomer()
        flash("Customer added successfully", 'success')
        return render_template('addcustomer.html')  # Redirect to the add customer page after adding
    return render_template('addcustomer.html')

@app.route('/customers/customerfinder', methods=['GET', 'POST'])
def search_customers():
    if request.method == 'POST':
        search_text = request.form['search_text']
        found_customers = customer_instance.customerFinder(search_text)
        return render_template('searchcustomer.html', found_customers=found_customers)
    return render_template('searchcustomer.html')

@app.route('/loans', methods=['GET'])
def displayLoans():
    all_loans = loan_instance.displayAllLoans()
    return render_template("displayloans.html", loans=all_loans)

@app.route('/loans/addloan', methods=['GET', 'POST'])
def addLoan():
    if request.method == 'POST':
        loan_instance.loan_book()
        return render_template('addloan.html')
    return render_template('addloan.html')

@app.route('/removeloan', methods=['POST'])
def removeLoan():
    book_id=request.form.get('book_id')
    print(book_id)
    loan_instance.return_book(book_id)
    flash("Loan Done",'success')
    return render_template('displayloans.html',loans=loan_instance.displayAllLoans())

@app.route('/loans/lateloans', methods=['GET'])
def displayLateLoans():
    all_late_loans = loan_instance.display_late_loans()
    return render_template("displaylateloans.html", late_loans=all_late_loans)

if __name__ == '__main__':
    app.run(debug=False)
