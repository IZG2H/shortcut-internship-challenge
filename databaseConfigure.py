def databaseConfigure(tableName, data):
    import sqlite3

    con = sqlite3.connect('expensesTracking.db')
    cur = con.cursor()
    cur.execute(f"CREATE TABLE '{tableName}'('name', 'amountNeededToPay', 'amountPaid')") #create a table
    cur.executemany(f"INSERT INTO '{tableName}' VALUES(?, ?, ?)", data) #insert the data from the function into the database
    con.commit()
    con.close()