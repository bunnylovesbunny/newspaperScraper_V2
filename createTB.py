


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

    # q4 = 'create table prothomalo (pa_id serial , pa_date date, pa_published varchar(255), pa_title varchar(255), pa_link varchar(255), constraint pa_id_pk primary key (pa_id));'
    # cursor.execute(q4)

    testCreate = 'create table sendbbc (sendbbc_id serial , sendbbc_date varchar(250), sendbbc_time time, sendbbc_published varchar(255), sendbbc_title varchar(255), sendbbc_link varchar(255), sendbbc_summary text, constraint sendbbc_id_pk primary key (sendbbc_id));'
    cursor.execute ( testCreate )

    testCreate = 'create table senddailystar (sendds_id serial , sendds_date varchar(250), sendds_time time, sendds_published varchar(255), sendds_title varchar(255), sendds_link varchar(255), sendds_summary text, constraint sendds_id_pk primary key (sendds_id));'
    cursor.execute(testCreate)

    testCreate = 'create table sendbanglatribune (senddt_id serial , senddt_date varchar(250), senddt_time time, senddt_published varchar(255), senddt_title varchar(255), senddt_link varchar(255), senddt_summary text,  constraint senddt_id_pk primary key (senddt_id));'
    cursor.execute(testCreate)

    testCreate = 'create table sendprothomalo (sendpa_id serial , sendpa_date varchar(250), sendpa_time time, sendpa_published varchar(255), sendpa_title varchar(255), sendpa_link varchar(255), sendpa_summary text,  constraint sendpa_id_pk primary key (sendpa_id));'
    cursor.execute(testCreate)



    # q_alter = 'alter table dailystar alter column ds_time type varchar(50)'
    # cursor.execute (q_alter)
    #
    # q_alter = 'alter table dailystar alter column ds_summary type text'
    # cursor.execute (q_alter)

    # q_alter = 'alter table bbc alter column bbc_time type varchar(50)'
    # cursor.execute(q_alter)
    #
    # q_alter = 'alter table bbc alter column bbc_summary type text'
    # cursor.execute(q_alter)
    #
    # q_alter = 'alter table banglatribune alter column dt_time type varchar(50)'
    # cursor.execute(q_alter)
    #
    # q_alter = 'alter table banglatribune alter column dt_summary type text'
    # cursor.execute(q_alter)
    #
    # q_alter = 'alter table prothomalo alter column pa_time type varchar(50)'
    # cursor.execute(q_alter)
    #
    # q_alter = 'alter table prothomalo alter column pa_summary type text'
    # cursor.execute(q_alter)

    # cursor.execute (q1)
    # cursor.execute (q2)
    # cursor.execute (q3)


    # duplicate_query = 'delete from banglatribune b1 using banglatribune b2 where b1.bt_id < b2.bt_id and b1.bt_title = b2.bt_title '
    # cursor.execute (duplicate_query)

    # drop_table = 'DROP TABLE BBC'
    # cursor.execute(drop_table)
    #
    # drop_table = 'DROP TABLE dailystar'
    # cursor.execute(drop_table)
    #
    # drop_table = 'DROP TABLE banglatribune'
    # cursor.execute(drop_table)
    #
    # drop_table = 'DROP TABLE prothomalo'
    # cursor.execute(drop_table)

    connection.commit()
    print("Table Created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")