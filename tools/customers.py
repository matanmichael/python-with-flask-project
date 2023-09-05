import sqlite3

from flask import render_template, request

class Customer:
    def __init__(self): 
        self.con = sqlite3.connect("library.db" ,check_same_thread=False)
        self.cur = self.con.cursor()
        self.cur.execute('''
                         CREATE TABLE IF NOT EXISTS customers
                         (id INTEGER PRIMARY KEY,
                         name TEXT,
                         city TEXT,
                         age INTEGER
                         )''')
        self.con.commit()
    
    def addNewCustomer(self):
        if request.method == 'POST':
            Name = request.form.get('name')
            City = request.form.get('city')
            Age = request.form.get('age')
            self.cur.execute('''
                INSERT INTO customers (name, city, age)
                VALUES (?, ?, ?)
            ''', (Name, City, Age))
            self.con.commit()
        return render_template("/addcustomer.html")
    
    def displayAllCustomers(self):
        self.cur.execute('SELECT * FROM customers')
        all_customers = self.cur.fetchall()
        return all_customers

    def removeCustomer(self, customer_id):
        try:
            self.cur.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
            self.con.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def customerFinder(self,search_text):
        self.cur.execute('''SELECT * FROM customers WHERE LOWER(name) LIKE?''', ('%' + search_text.lower() + '%',))
        found_customers=self.cur.fetchall()
        return found_customers

    def close(self):
        self.con.close()


