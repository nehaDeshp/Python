import pymysql
db=None

#def add(name,age,sal)
try:
    db = pymysql.connect(host="localhost", user="root", password="root",db="demo",charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
except ConnectionError as c:
    print("Connection Error")
    c.__traceback__()
else:
    print("Success !!!")
    cursor=db.cursor()

    if __name__ == '__main__':
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Exit")

        while(True):
            option = int(input("Enter your option : "))
            if(option == 1):
                name = input("Enter name")
                age = int(input("Enter Age"))
                sal = int(input("Enter Salary"))
                cursor.execute("insert into `employee` (`ename`,`age`,`sal`) values(%s,%s,%s)",(name,age,sal))
                db.commit()
            elif (option == 2):
                name = input("Enter Name to delete")
                cursor.execute("delete from `employee` where ename=%s",name)
                db.commit()
            elif(option == 3):
                name = input("Enter Name as Key : ")
                val = input("Enter salary to Update  :")
                cursor.execute("update employee set sal = %s where ename = %s",(val,name))
            elif(option == 4):break
            else: print("Invalid option")
finally:
    if(db != None):
        db.close()

