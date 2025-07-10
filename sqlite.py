import sqlite3

# Connect to SQLite
connection = sqlite3.connect("finance.db")

# Create a cursor object to insert records and create table
cursor = connection.cursor()

# Create the transactions table
table_info = """
CREATE TABLE TRANSACTIONS (
    TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DATE TEXT,
    DESCRIPTION TEXT,
    AMOUNT REAL,
    TYPE TEXT, -- 'debit' or 'credit'
    CATEGORY TEXT,
    ACCOUNT TEXT
)
"""

cursor.execute(table_info)

# Insert sample financial records
cursor.execute("""INSERT INTO TRANSACTIONS (DATE, DESCRIPTION, AMOUNT, TYPE, CATEGORY, ACCOUNT)
                  VALUES ('2025-07-01', 'Salary Credited', 50000, 'credit', 'Income', 'HDFC')""")

cursor.execute("""INSERT INTO TRANSACTIONS (DATE, DESCRIPTION, AMOUNT, TYPE, CATEGORY, ACCOUNT)
                  VALUES ('2025-07-03', 'Grocery Store', -2500, 'debit', 'Groceries', 'HDFC')""")

cursor.execute("""INSERT INTO TRANSACTIONS (DATE, DESCRIPTION, AMOUNT, TYPE, CATEGORY, ACCOUNT)
                  VALUES ('2025-07-05', 'Amazon Purchase', -3200, 'debit', 'Shopping', 'ICICI')""")

cursor.execute("""INSERT INTO TRANSACTIONS (DATE, DESCRIPTION, AMOUNT, TYPE, CATEGORY, ACCOUNT)
                  VALUES ('2025-07-10', 'Freelance Payment', 12000, 'credit', 'Side Income', 'Paytm')""")

cursor.execute("""INSERT INTO TRANSACTIONS (DATE, DESCRIPTION, AMOUNT, TYPE, CATEGORY, ACCOUNT)
                  VALUES ('2025-07-11', 'Electricity Bill', -1800, 'debit', 'Utilities', 'HDFC')""")

# Display inserted records
print("The inserted finance records are:")
data = cursor.execute('''SELECT * FROM TRANSACTIONS''')
for row in data:
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()

