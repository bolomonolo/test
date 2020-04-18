import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)


user = (1,'jose', 'asdf')

users [
    (4,'jose', 'asdf')
    (2,'jose', 'asdf')
]

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query,user)

cursor.executemany(insert_query, users)

connection.commit()

connection.close()
