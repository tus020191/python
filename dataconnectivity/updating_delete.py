import mysql.connector as connector
try:

    conn = connector.connect(host="localhost", user="root",password="",database="practice")
    conn.Autocommit="of"
    print("successful!!!")
except:
    print("unsuccessful!!!!")
    exit("retry")

print(conn.is_connected())
cur =conn.cursor()


try:

    sql="update student " \
         "set s_no=300 where name='tansihk' "
    cur.execute(sql)
    print(f"rows affected :-  {cur.rowcount}")
        

    sql="update student " \
        "set s_no =400" \
        " where name ='tarun' "

    cur.execute(sql)

    print("yes")
    print(f"rows affected :-  {cur.rowcount}")

    sql="delete from student " \
        "where name='vishal' "
    cur.execute(sql)
    print(f"rows affected :-  {cur.rowcount}")




    conn.commit()

except:
    print("retry not able to update")
    conn.rollback()


cur.close()
conn.close()
