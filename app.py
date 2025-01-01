import sqlite3 #import sqlite3 library

#CONNECT TO OR CREATE THE DATABASE FILE
conn = sqlite3.connect('inventory.db')

#CREATE THE CURSOR OBJECT TO INTERACT WITH THE DATABASE
cursor = conn.cursor()

# use cursor to create sql table items
cursor.execute('''
      CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INT NOT NULL,
        reorder_level INT NOT NULL,
        location TEXT   
      )         
''')
conn.commit()

cursor.execute("INSERT INTO items (name, quantity, reorder_level, location) VALUES (?,?,?, ?)", ('HDMI CABLE', 10, 5, 'ODale'))

