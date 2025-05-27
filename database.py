import sqlite3
#connect to a database(creates one if it doesn't exist)
conn= sqlite3.connect('mydatabase.db')

#Create a cursor object using the cursor() method to execute SQL commands
cursor = conn.cursor()
#Create a table
cursor.execute('''
              CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY ,
                  username TEXT NOT NULL,
                  age INTEGER,
                  email TEXT UNIQUE
              )
              ''')
#Insert data into the table
#cursor.execute('''
             # INSERT INTO users (username, age, email)
              #VALUES ('john_doe', 30, 'john@example.com')
              #''')

# insert multiple records
users = [
    ('jane_doe', 25, 'jane@example.com'),
    ('alice_smith', 28, 'alice@example.com'),
    ('bob_jones', 32, 'bob@example.com')
]
cursor.executemany('''
    INSERT OR IGNORE INTO users (username, age, email)
    VALUES (?, ?, ?)
''', users)

conn.commit()  # Commit the changes to the database

#retieve data from the table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()  # Fetch all rows from the executed query
for row in rows:
    print(row)
    print(type(row))

#retireve records with specific condition
cursor.execute('SELECT * FROM users WHERE age > 28')
rows = cursor.fetchall()
for row in rows:
    print(row)
    print(type(row))

#UPDATING RECORDS
cursor.execute('''
    UPDATE users
    SET age = 29
    WHERE username = 'jane_doe'
''')
conn.commit()  # Commit the changes

#DELETE RECORDS
cursor.execute('''
    DELETE FROM users
    WHERE username = 'bob_jones'
''')
conn.commit()  # Commit the changes

cursor.close()  # Close the cursor
conn.close()  # Close the database connection
# To ensure the database is created and the table is set up, you can run this script once.
# After running, you can comment out the table creation part to avoid errors on subsequent runs.
# You can also uncomment the insert statement to add a new user if needed.
