import mysql.connector

sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pysql"
)

def barang(name,stock,price):
    cursor = sql.cursor()

    insert = 'INSERT INTO barang (name,stock,price) VALUES (%s,%s,%s)'
    value = name,stock,price
    cursor.execute(insert,value)

    sql.commit()

    if cursor.rowcount > 0:
        print('\nData add succesfully\n')
    else:
        print('\nNot add succesfully\n')

def view():
    cursor = sql.cursor()

    select='SELECT * FROM barang'
    cursor.execute(select)
    return cursor.fetchall()

def Builtin():
    cursor = sql.cursor()

    select="SELECT price FROM barang"
    cursor.execute(select)
    return cursor.fetchall()



