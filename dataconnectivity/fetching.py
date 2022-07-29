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

try:
    sql="select * from student"
    cur.execute(sql)


    print("s_no\t\t\tname\t\t\taddress\n","*"*70)
    for rows in cur:
        print(f"*\t{rows[0]}\t*\t\t{rows[1]}\t*\t\t{rows[2]}")

    sql = "select * from student"
    cur.execute(sql)
    ### fetchone method
    row=cur.fetchone()
    print(f" using fetchone row= {row} ")
    #### fetchmany
    ### with fetchmany be careful as
    ### if all rows are not fetched prior to
    ### closing of connection then error " unread result found " occur
    rows=cur.fetchmany(3)
    print(f" \n\nusing fetchmany rows : \n")
    for i in rows :
        print(i)
    rows=cur.fetchall()
    print(f" \n\nusing fetchall for remaining  rows : ")
    for i in rows:
        print(i)


except:
    print('not able to fetch data')

cur.close()
conn.close()