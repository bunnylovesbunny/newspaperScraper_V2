DB_HOST = "127.0.0.1"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "123456"

import psycopg2
from datetime import datetime

# connection = psycopg2.connect (user="postgres" ,
#                                password="123456" ,
#                                host="127.0.0.1" ,
#                                port="5432" ,
#                                database="postgres")
#
# # Create a cursor to perform database operations
# cursor = connection.cursor ()
#
#
# connection.close()

import psycopg2
from psycopg2 import Error


try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    # # Create a cursor to perform database operations
    cursor = connection.cursor()
    # # Print PostgreSQL details
    # print("PostgreSQL server information")
    # print(connection.get_dsn_parameters(), "\n")
    # # Executing a SQL query
    # cursor.execute("SELECT version();")
    # # Fetch result
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

    # SQL query to create a new table
    # create_table_query = '''CREATE TABLE bbc
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       DATE DATE NOT NULL,
    #       TITLE       TEXT   ,
    #       LINK         TEXT,
    #       PUBLISHED TEXT NOT NULL
    #       ); '''
    # # Execute a command: this creates a new table
    # cursor.execute(create_table_query)
    now = datetime.now ()
    current_time = now.strftime ("%H:%M:%S")
    # q = "create table bbc (id serial primary key, date date not null, title text, link text, published text )"
    # insert_query = """ INSERT INTO bbc (ID, DATE, TITLE, LINK, PUBLISHED) VALUES (1,12/12/2020,
    # 'Trump impeached for inciting US Capitol riot',
    # 'https://www.bbc.co.uk/news/world-us-canada-55656385',
    # '2021-01-14T02:52:31'
    #       )"""
    # q = "insert into bbc (date, title, link, published) values ('2020-12-12', 'asbcerdfg','https://pynative.com/python-postgresql-tutorial/','1234TO123')"

    q = "select * from bbc"
    cursor.execute (q)
    print("resutl", cursor.fetchall())


    connection.commit()
    print("Table created successfully in PostgreSQL ")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")