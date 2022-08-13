import mysql.connector as connector
try:

    conn = connector.connect(host="localhost", user="root",password="",database="practice")
    conn.Autocommit="on"
    print("successful!!!")
except:
    print("unsuccessful!!!!")
    exit("retry")

print(conn.is_connected())
cur =conn.cursor()
sql="show tables"
cur.execute(sql)
for i in cur:
    print(i)
"""
        ---------------------- CREATNG TABLE-------------------------------------------------
"""

try:
    sql="""create table student
    (
        s_no INT NOT NULL  ,
        name varchar(30),
        address varchar(30)
    )
    """

    cur.execute(sql)

except:
    print("not able to create table!!!!")

