import sqlite3

con = sqlite3.connect('tutorial.db') #this creates a connection with tutorial.db. if dh then it will create one
cur = con.cursor() #it is used to execute and fetch results from sql queries
cur.execute('CREATE TABLE movie(title, year, score)')
cur.execute("""INSERT INTO movie VALUES('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for Something Completely Different', 1971, 7.5)""")