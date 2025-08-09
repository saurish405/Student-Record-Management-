import mysql.connector as sqltor
print("Programing Language Details")
def Insert():
    mycon = sqltor.connect(host='localhost',user='root',passwd='root',database='programming_language')
    lid = int(input("Enter Language ID:- "))
    name = input("Enter Language Name:- ")
    cname = input("Enter Creator Name:- ")
    rdate = input("Enter Relese Date:- ")
    version= int(input("Enter Version:- "))
    rating = int(input("Enter Ratings:-"))
    qry = "insert into program values({},'{}','{}','{}',{},{})".format(lid,name,cname,rdate,version,rating)
    cur = mycon.cursor()
    cur.execute(qry)
    mycon.commit()
    mycon.close()
def Delete():
    mycon = sqltor.connect(host='localhost',user='root',passwd='root',database='programming_language')
    cur = mycon.cursor()
    lid = int(input("Enter ID:- "))
    qry = "delete from program where lid = {}".format(lid)
    cur.execute(qry)
    mycon.commit()
    mycon.close()
def UpdateRatings():
    mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="programming_language")
    cur = mycon.cursor()
    marks = int(input("Enter Ratings to be Updated (+ sign For Incr/- Sign for Decre)"))
    lid = int(input("Enter lid:- "))
    qry = "update program set rating = rating + {} where lid={}".format(rating,lid)
    cur.execute(qry)
    mycon.commit()
    mycon.close()
def ShowAll():
    mycon = sqltor.connect(host='localhost',user='root',passwd='root',database='programming_language')
    cur = mycon.cursor()
    qry = "select * from program"
    cur.execute(qry)
    data = cur.fetchall()
    for rec in data:
        print(rec)
        mycon.close()
def Search_ID():
    mycon = sqltor.connect(host="localhost",user="root",passwd="root",database='programming_language')
    cur = mycon.cursor()
    lid = int(input("Enter Language ID:- "))
    qry = "select * from program where lid = {}".format(lid)
    cur.execute(qry)
    data = cur.fetchall()
    if len(data)==0:
        print("Record Not Found")
    else:
        for rec in data:
            print(rec)
    mycon.close()
#___Main___
while True:
    print("Programming Laguage Details")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Update Rating Record")
    print("4. Search Record On Based ID")
    print("5. Show All Records")
    print("6. Exit")
    choice = int(input("Enter Your Choice:- "))
    if choice==1:
        Insert()
    elif choice==2:
        Delete()
    elif choice==3:
        UpdateRatings()
    elif choice==4:
        Search_ID()
    elif choice==5:
        ShowAll()
    elif choice==6:
        break
    else:
        print("Wrong Choice, Try Again!!!")
