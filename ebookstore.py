import sqlite3

db = sqlite3.connect('Capstone/ebookstore')

cursor = db.cursor()

cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty TEXT)''')

db.commit()

cursor = db.cursor()

id2 = 3001
title2 = 'A Tale of Two Cities'
author2 = 'Charles Dickens'
qty2 = 30

id3 = 3002
title3 = 'Harry Potter and the Philosophers Stone'
author3 = 'J.K Rowling'
qty3 = 40

id4 = 3003
title4 = 'The Lion, the Witch and the Wardrobe'
author4 = 'C.S Lewis'
qty4 = 25

id5 = 3004
title5 = 'The Lord of the Rings'
author5 = 'J.R.R Tolkien'
qty5 = 37

id6 = 3005
title6 = 'Alice in Wonderland'
author6 = 'Lewis Carroll'
qty6 = 12

bookss = [(id2,title2,author2,qty2),(id3,title3,author3,qty3),(id4,title4,author4,qty4),(id5,title5,author5,qty5),(id6,title6,author6,qty6)]
cursor.executemany('''INSERT INTO books(id,title,author,qty)
VALUES(?,?,?,?)''',bookss)

print('All users inserted')
db.commit()
