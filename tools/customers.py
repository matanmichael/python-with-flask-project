import sqlite3

class Customer:
    def __init__(self): 
        self.con = sqlite3.connect("library.db" )
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
        Name=input("add customer name: ")
        City=input("add customer city: ")
        Age=input("add customer age: ")
        self.cur.execute('''
        INSERT INTO customers (name,city,age)
        VALUES(?,?,?)
        ''',(Name,City,Age)
        )    
        self.con.commit()

    def displayAllCustomers(self):
        self.cur.execute('''SELECT * FROM customers''')
        customers_list=self.cur.fetchall()
        for customer in customers_list:
            return customer

    def removeCustomer(self):
        print("Customer Remove")
        target_id=input("target id: ")
        self.cur.execute('''DELETE FROM customers WHERE id=?''',(target_id,))
        self.con.commit
        if self.cur.rowcount > 0:
            print(f"Book with ID {target_id} removed.")
        else:
            print(f"Book with ID {target_id} not found.")

    def customerFinder(self):
        print("Customer Search")
        search_text = input("Enter Customer Name: ")
        self.cur.execute('''SELECT * FROM cutomers WHERE LOWER(name) LIKE?''', ('%' + search_text.lower() + '%',))
        found_customers=self.cur.fetchall()
        for customer in found_customers:
            return customer
        
    def close(self):
        self.con.close()


