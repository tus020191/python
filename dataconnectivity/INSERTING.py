import mysql.connector as connector
try:

    conn = connector.connect(host="localhost", user="root",password="",database="practice")
    conn.Autocommit="on"
    print("successfully connected !!!")
except:
    print("unsuccessful!!!!")
    exit("retry")

print(conn.is_connected())
"""prepared ="True"  make cursor as mysql cursor prepared"""
cur =conn.cursor()

def insert(name,s_no,address):
    try:
        sql = "insert into student(address, name, s_no)" \
              "Values(%(address)s, %(name)s,%(roll)s) "
        parameter={"name" : name,
                   "address" :address,
                   "roll" : s_no}
        cur.execute(sql,parameter)

        conn.commit()

        print("successfull inserted : ")
        print(f"total rows affected : {cur.rowcount}")
    except:
        print("not inserted !!!")
        conn.rollback()

try:
    while(True):
        name=input("enter name :\t\t\t\t")
        address = input("enter address :\t\t\t\t")
        roll=int(input("enter roll no:\t\t\t\t"))
        insert(name,roll,address)
        print("do you want to continue(y/n): ",end=" ")
        c=input("")
        print("\n\n")
        if(c=="n"):
            break


except:
    print("plz enter valid values!!!!")


"""
try:

    
    sql = "insert into student(address, name, s_no)"\
          "Values('mansarovar', 'vishwas', 900), ('kota', 'shreya', 800),('civil lines', 'vishal', 700) "
    
    cur.execute(sql)
    conn.commit()

    print("successfull")
    print(f"total rows affected : - {cur.rowcount}")
    
    
   
    
except:
    conn.rollback()
    print("cannot insert values into tables!!!!!")
"""
cur.close()
conn.close()
