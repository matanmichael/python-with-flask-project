from flask import Flask, render_template, request
from tools.books import Book
from tools.customers import Customer
from tools.loans import Loan 

book_instance=Book()
customer_instance=Customer()
loan_customer=Loan()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addbook', methods=['GET', 'POST'])
def addBook():
    return book_instance.addNewBook()

@app.route('/books', methods=['GET'])
def displayBooks():
    return book_instance.DisplayAllBooks()

@app.route('/removebook', methods=['GET', 'POST'])
def remove_book(book_id):
    result = None

    if request.method == 'POST':
        result = book_instance.removeBook(book_id)

    book_instance.close()
    return render_template("removebook.html", result=result)



    
if __name__ == '__main__':
    app.run(debug=True)
