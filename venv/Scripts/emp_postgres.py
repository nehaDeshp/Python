import psycopg2

db = None
try:
    db = psycopg2.connect(database="employeeData",user=root, password=root, host=localhost, port=db_port)
except:
    print("Error!!")
finally:
    if(db!=None):
        db.close()