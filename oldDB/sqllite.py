import sqlite3
# Build Database
dbfile = "database1.db"
con = sqlite3.connect(dbfile)

# Create database Cursor variables
cursorObj = con.cursor()
print('Connect OOOk')


# Build Table
# seed (ID, SEEDID, X, Y, Z, N, E, battery, STATUS)
cursorObj.execute(
'''CREATE TABLE seed
(id INTEGER PRIMARY KEY NOT NULL,
seedID INTEGER ,
x REAL ,
y REAL ,
z REAL ,
n decimal(10, 7) ,
e decimal(10, 7) ,
battery INTEGER ,
status INTEGER ); ''')

print('SEEDS Table created.')
con.commit()


# Insert
cursorObj.execute('''INSERT INTO seed (ID, SEEDID, X, Y, Z, N, E, battery, STATUS) VALUES (1, 9527, 3.14, -1314.97, 116.666 , 22.998328, 120.218582, 32, 1)''')

cursorObj.execute('''INSERT INTO seed (ID, SEEDID, X, Y, Z, N, E, battery, STATUS) VALUES (2, 9497, -191.1, -110.113 , -114.666 , 22.998328, 120.218582, 99,2)''')
con.commit()
print('Insert ok')

# Select
results = cursorObj.execute('''SELECT * FROM seed''')
for item in results:
    print(item)
con.close()	