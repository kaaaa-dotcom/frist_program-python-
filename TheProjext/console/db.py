# ini adalah pembuatan mysql-python
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='absend'
)

def add_members(nomor,nama,gender):
    Thecursor = db.cursor()

    insert =('INSERT INTO members (nomor,nama,gender) VALUES (%s,%s,%s)')
    value =(nomor,nama,gender)
    Thecursor.execute(insert,value)

    db.commit()

    if Thecursor.rowcount > 0:
        print('\nMembers Berhasil Ditambahkan\n')
    else:
        print('\nMembers Gagal Ditambahkan\n')

def check():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM members')
    return cursor.fetchall()

def Delete(ID):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM members WHERE `members`.`id` = {ID}")

    db.commit()

    print(cursor.rowcount,'\nData berhasil dihapus...!')