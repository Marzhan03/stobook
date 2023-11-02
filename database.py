import sqlite3
import random
conn=sqlite3.connect('db.sqlite3')
cursor=conn.cursor()
for i in range (1571):
    cost_massiv=[]
    cost = random.randint(200, 600)
    cost_massivs=(cost)

    cursor.execute(f"INSERT INTO book_book (cost) VALUES (?)",(cost_massivs,))
    conn.commit()
    conn.close()
