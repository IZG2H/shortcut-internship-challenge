import sqlite3

def databaseInsert(tableName, data): #if got time, add in creation time logs
    import sqlite3

    con = sqlite3.connect('expensesTracking.db')
    cur = con.cursor()
    #add a popup that disallow repeated names
    cur.execute(f'''CREATE TABLE IF NOT EXISTS '{tableName}'(
                        name TEXT, 
                        amountNeededToPay REAL, 
                        amountPaid REAL
                )''') #create a table
    cur.executemany(f"INSERT INTO '{tableName}' VALUES(?, ?, ?)", data) #insert the data from the function into the database
    con.commit()
    con.close()

def updateData(): #
    import sqlite3

    con = sqlite3.connect('expensesTracking.db')
    cur = con.cursor()
    # cur.execute(f"SELECT * from {name}")