import sqlite3
from flask import request

class Book:
    def __init__(self):
        self.connection = sqlite3.connect("library.db",check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY UNIQUE,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                type TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    
    def addNewBook(self):
        Name=request.form.get('name')
        Author =request.form.get('author')
        YearPublished=request.form.get('yearPublished')
        Type=request.form.get('type')
        self.cursor.execute('''
                    INSERT INTO books ( title, author, year, type)
                    VALUES ( ?, ?, ?, ?)
                ''', ( Name, Author, YearPublished, Type))
        self.connection.commit()
            
    def DisplayAllBooks(self):
        self.cursor.execute('SELECT * FROM books')
        all_books = self.cursor.fetchall()
        return all_books

    def removeBook(self, book_id):
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.connection.commit()
        
    def bookFinder(self,search_text):
        self.cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ?', ('%' + search_text.lower() + '%',))
        found_books = self.cursor.fetchall()
        return found_books
        
    def close(self):
        self.connection.close()

