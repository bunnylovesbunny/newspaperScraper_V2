


import psycopg2
from psycopg2 import Error
from psycopg2 import sql

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    # SQL query to create a new table

    # newspapers = [  'thedailystar' , 'banglatribune' ]
    # for i in newspapers:
    #     create_table_query = ("CREATE TABLE {} (id serial, date date, published varchar(255), title varchar(255), link varchar(255))".format(sql.Identifier(i)))
    #     cursor.execute(create_table_query,i)
    #
    # newspaper = ('thedailystar','banglatribune')
    # create_table_query = '''CREATE TABLE %s
    #                 (ID SERIAL    NOT NULL,
    #                   DATE          DATE ,
    #                   PUBLISHED     VARCHAR(255),
    #                   TITLE VARCHAR(255)
    #                   LINK VARCHAR(255)); '''
    # cursor.execute(create_table_query,newspaper)



    # create_table_query = '''CREATE TABLE mobile
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       MODEL           TEXT    NOT NULL,
    #       PRICE         REAL); '''
    # # Execute a command: this creates a new table


    # q1 = 'create table bbc (bbc_id serial , bbc_date date, bbc_published varchar(255), bbc_title varchar(255), bbc_link varchar(255), constraint bbc_id_pk primary key (bbc_id));'
    # q2 = 'create table dailystar (ds_id serial , ds_date date, ds_published varchar(255), ds_title varchar(255), ds_link varchar(255), constraint ds_id_pk primary key (ds_id));'
    # q3 = 'create table banglatribune (bt_id serial , bt_date date, bt_published varchar(255), bt_title varchar(255), bt_link varchar(255), constraint bt_id_pk primary key (bt_id));'
    #
    # cursor.execute (q1)
    # cursor.execute (q2)
    # cursor.execute (q3)


    duplicate_query = 'delete from banglatribune b1 using banglatribune b2 where b1.bt_id < b2.bt_id and b1.bt_title = b2.bt_title '
    cursor.execute (duplicate_query)

    # drop_table = 'DROP TABLE BBC'
    # cursor.execute(drop_table)

    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")