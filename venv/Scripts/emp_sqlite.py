import sqlite3

db=None
try:
    db=sqlite3.connect("empDemo.db")
    db.execute("Create table if NOT EXISTS `employee`(ename text,age integer,sal integer)")
except:
    print("Connection Error !")
else:
    if __name__ == '__main__':
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Exit")
    while (True):
        option = int(input("Enter your option : "))
        if (option == 1):
            name = input("Enter name")
            age = int(input("Enter Age"))
            sal = int(input("Enter Salary"))
            db.execute("insert into `employee` (`ename`,`age`,`sal`) values(?,?,?)", (name, age, sal))
            db.commit()
        elif (option == 2):
            name = input("Enter Name to delete")
            db.execute("delete from `employee` where ename=?", (name,))
            db.commit()
        elif (option == 3):
            name = input("Enter Name as Key : ")
            val = input("Enter salary to Update  :")
            db.execute("update employee set sal = ? where ename = ?", (val, name))
            db.commit()
        elif (option == 4):
            break
        else:
            print("Invalid option")
finally:
    if(db!=None):
        db.close()