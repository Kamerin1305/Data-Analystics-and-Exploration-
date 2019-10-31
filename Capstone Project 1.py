import sqlite3

db = sqlite3.connect('Capstone/ebookstore')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty TEXT)''')
db.commit()

def add():
    id1 = int(input("Enter the book ID: "))
    title = input("Enter the book Title: ")
    auth = input("Enter the Book Author: ")
    qty = int(input("Enter the book qty: "))
    books = [(id1, title, auth, qty)]
    cursor.executemany('''INSERT INTO books(id,Title,Author,Qty)Values(?,?,?,?)''', books)
    db.commit()

def update():
    d = int(input("USing the books id, Which bvooks title would you like to update? : "))
    a = str(input("Change the Title of the book: "))
    cursor.execute(f'''UPDATE books SET Title = "{a}" WHERE id = {d}''')
    db.commit()
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    print(books)

def delete():
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    print(books)
    f = int(input("Using the id which book would youy like to delete? : "))
    cursor.execute(f'''DELETE FROM books WHERE id = {f}''')
    db.commit()

def search():
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    print(books)
    c = int(input("Search for a book using its id"))
    cursor.execute(f'''SELECT * FROM books WHERE id = {c}''')
    books = cursor.fetchone()
    print(books)

def menu():
    while True:
        u = int(input("What would you like to do: \n1. Enter Book \n2. Update Book \n3. Delete Book \n4. Search Book \n0. Exit"))
        if u == 1:
            add()
        elif u == 2:
            update()
        elif u == 3:
            delete()
        elif u == 4:
            search()
        elif u == 0:
            break
        else:
            print("Invalid input")

menu()
    
    

