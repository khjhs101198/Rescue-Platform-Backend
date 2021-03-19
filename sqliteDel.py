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


# Delete
sql = """
   delete from collection where id = 1
"""
db.engine.execute(sql)
print('Insert ok')

# Select
results = cursorObj.execute('''SELECT * FROM seed''')
for item in results:
    print(item)
con.close()	