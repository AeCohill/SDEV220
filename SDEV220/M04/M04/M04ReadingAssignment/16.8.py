## 16.8 Use the sqlalchemy module to 
# connect to the sqlite3 database books.db 
# that you just made in exercise 16.4. 
# As in 16.6, select and print 
# the title column from the book table in alphabetical order.

import sqlalchemy as sa

engine = sa.create_engine('sqlite:///books.db')

conn = engine.connect()

meta = sa.MetaData()

books_table = sa.Table('books', meta, autoload=True, autoload_with=engine)
select_q = sa.select([books_table.columns.title]).order_by(books_table.columns.title)

res = conn.execute(select_q)

for row in res:
    print(row[0])
    
conn.close()
