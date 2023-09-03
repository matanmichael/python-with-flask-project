import sqlite3
from flask import render_template, request

class Book:
    def __init__(self):
        self.connection = sqlite3.connect("library.db",check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                type TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    
    def addNewBook(self):
        if request.method=='POST':
            Name=request.form.get('name')
            Author =request.form.get('author')
            YearPublished=request.form.get('yearPublished')
            Type=request.form.get('type')
            self.cursor.execute('''
                INSERT INTO books ( title, author, year, type)
                VALUES ( ?, ?, ?, ?)
            ''', ( Name, Author, YearPublished, Type))
            self.connection.commit()
        return render_template("/addbook.html")
    
    def DisplayAllBooks(self):
        self.cursor.execute('SELECT * FROM books')
        all_books = self.cursor.fetchall()
        print(all_books)
        return render_template("displaybooks.html", books=all_books)

    def removeBook(self):
        target_id=input("target id: ")
        self.cursor.execute('DELETE FROM books WHERE id = ?', (target_id,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print(f"Book with ID {target_id} removed.")
        else:
            print(f"Book with ID {target_id} not found.")

    def bookFinder(self):
        search_text = input("Enter Book Name: ")
        self.cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ?', ('%' + search_text.lower() + '%',))
        found_books = self.cursor.fetchall()
        for book in found_books:
            return book
    def close(self):
        self.connection.close()

