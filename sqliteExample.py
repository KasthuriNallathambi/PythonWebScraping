import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor() # objects executes sql query

#Query all the data
cursor.execute("SELECT * FROM events")
results = cursor.fetchall()
print(results)

#Query based on the column
cursor.execute("SELECT * FROM EVENTS WHERE band='Tigers'")
results = cursor.fetchall()
print(results)

#insert new rows
new_rows = [('Cats','Cat City','2028-08-07'),
            ('Dogs','Dog City','2029-09-06')
            ]

cursor.executemany("INSERT INTO EVENTS VALUES (?,?,?)",new_rows)
connection.commit() #write the changes after insertion