def databaseInsert(tableName, data): #if got time, add in creation time logs
    import sqlite3
    from tkinter import messagebox

    con = sqlite3.connect('expensesTracking.db')
    cur = con.cursor()
    #makes the table not create if there is ald another table with the same name
    cur.execute(f'''CREATE TABLE IF NOT EXISTS '{tableName}'(
                    name TEXT, 
                    amountNeededToPay REAL, 
                    amountPaid REAL
                )''') #create a table
    cur.executemany(f"INSERT INTO '{tableName}' VALUES(?, ?, ?)", data) #insert the data from the function into the database
    con.commit()
    con.close()
