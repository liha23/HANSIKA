import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)
mycursor = mydb.cursor()

def add_employee():
    eid = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    basic = int(input("Enter Basic Salary: "))
    allow = int(input("Enter Allowance: "))
    total = basic + allow
    sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    val = (eid, name, basic, allow, total)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Employee Record Added Successfully")

def display_employee():
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchall()
    for row in result:
        print(row)

def update_salary():
    eid = int(input("Enter Employee ID: "))
    basic = int(input("Enter New Basic Salary: "))
    allow = int(input("Enter New Allowance: "))
    total = basic + allow
    sql = "UPDATE employee SET basic_salary=%s, allowance=%s, total_salary=%s WHERE emp_id=%s"
    val = (basic, allow, total, eid)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Salary Updated Successfully")

def delete_employee():
    eid = int(input("Enter Employee ID to Delete: "))
    sql = "DELETE FROM employee WHERE emp_id=%s"
    val = (eid,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Employee Record Deleted Successfully")

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_employee()
    elif ch == 2:
        display_employee()
    elif ch == 3:
        update_salary()
    elif ch == 4:
        delete_employee()
    elif ch == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
