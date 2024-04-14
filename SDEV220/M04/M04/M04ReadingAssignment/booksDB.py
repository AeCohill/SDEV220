## create a SQLite database called books.db and a table called 
# books with these fields: title (text),
# author (text), and year

import sqlite3
conn = sqlite3.connect(books.db)
curs = conn.cursor()
curs.execute('''CREATE TABLE books
             (title STR,
             author STR,
             year INT) ''')

## had chatGPT give rando data and i wrote this to pop the DB
data_to_insert = [
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]    

curs.executemany("INSERT INTO books VALUES (?, ?, ?)", data_to_insert)
    
curs.close()
conn.close()