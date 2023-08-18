import sys

import pyodbc

conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\carpeta\Database111111.accdb;")

cursor=conn.cursor()

cursor.execute("SELECT * FROM clase3")

for row in cursor.fetchall():

    print(row)

cursor.close

conn.close