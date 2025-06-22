import sqlite3

from werkzeug.serving import connection_dropped_errors

from main import connection, cursor

connection = sqlite3.connect("sqlite.db")
cursor= connection. cursor()
cursor.execute('''
    insert into like (id,post_id,user_id) values (1,1,1);
        ''')

connection.commit()
connection.close()