import sqlite3
from datetime import datetime, timedelta

class Loan:
    def __init__(self):
        self.con=sqlite3.connect("library.db")
        self.cur=self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS loans(
                id INTEGER PRIMARY KEY,
                LoanDate TEXT,
                ReturnDate TEXT,
                CustID INTEGER,
                BookID INTEGER,
                FOREIGN KEY (CustID) REFERENCES customers(id),
                FOREIGN KEY (BookID) REFERENCES books(id)
            )
        ''')
    def displayAllLoans(self):
        self.cur.execute('''SELECT * FROM loans ''')
        all_loans=self.cur.fetchall()
        print(all_loans)

    def loan_book(self):
        # Input from the user
        cust_id = input("Enter Customer ID: ")
        book_id = input("Enter Book ID: ")
        loan_date = datetime.now().strftime('%Y-%m-%d')  # Get the current date

        # Retrieve book type from the database

        self.cur.execute("SELECT Type FROM books WHERE Id=?", (book_id,))
        book_type = int(self.cur.fetchone()[0])

        # Set return date based on book type
        if book_type == 1:
            return_date = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')
        elif book_type == 2:
            return_date = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
        elif book_type == 3:
            return_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        else:
            print("Invalid book type.")
            return
        self.cur.execute('''
            INSERT INTO loans (CustID, BookID, Loandate, Returndate)
            VALUES (?, ?, ?, ?)
        ''', (cust_id, book_id, loan_date, return_date))
        self.con.commit()

        print("Book has been successfully loaned!")


    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        # Check if the book is currently on loan and has a non-null return date
        self.cur.execute("SELECT * FROM loans WHERE BookID=? AND ReturnDate IS NOT NULL", (book_id,))
        loan_record = self.cur.fetchone()

        if not loan_record:
            print("Book is not currently on loan or has already been returned.")
            return

        # Delete the loan record for the returned book
        self.cur.execute("DELETE FROM loans WHERE BookID=?", (book_id,))
        self.con.commit()

        print(f"Book with ID {book_id} has been returned and loan record has been removed.")
    
    def display_late_loans(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.cur.execute("SELECT * FROM loans WHERE ReturnDate < ? AND ReturnDate IS NOT NULL", (current_date,))
        late_loans = self.cur.fetchall()

        if not late_loans:
            print("No late loans found.")
            return

        print("Late Loans:")
        for loan in late_loans:
            print(f"Loan ID: {loan[0]}, Customer ID: {loan[3]}, Book ID: {loan[4]}, Return Date: {loan[2]}")

