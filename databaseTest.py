import sqlite3

con = sqlite3.connect('tutorial.db') #this creates a connection with tutorial.db. if dh then it will create one
cur = con.cursor() #it is used to execute and fetch results from sql queries
cur.execute('CREATE TABLE movie(title, year, score)')
cur.execute("""INSERT INTO movie VALUES('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for Something Completely Different', 1971, 7.5)""")
con.commit() #always commit after execute command
data = [('Monty Python Live at the Hollywood Bowl', 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's The Live of Brian", 1979, 8.0)] #this is to insert multiple data
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data) #this is preferred to avoid sql injection attacks
con.commit()
con.close()