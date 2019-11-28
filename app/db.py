import pyodbc
conn_str=(
    'Driver={SQL Server};'
    'Server=DESKTOP-IF5CCEF\TESTINSTANCE;'
    'Database=lab6_b;'
    'Trusted_Connection=yes;'
)
cnxn=pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute("SELECT fname FROM Employee")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.fname)
cnxn.close()