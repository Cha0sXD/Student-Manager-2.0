# Importing Modules
import mysql.connector

# Connecting to SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Doctor@10th",
    database = "Main")
cursor = db.cursor()

#Classes
class Person():
    def finding_person():
        query = """
        
"""

class Student():
    pass

class teacher():
    pass

class admin():
    pass

#Main Function
def main_dash():
    print("\n========================================\n" \
          "             STUDENT MANAGER              \n" \
          "========================================\n\n" \
          "1. Student Login\n" \
          "2. Teacher Login\n" \
          "3. Admin Login\n" \
          "4. Exit\n")
    query = input("Enter The Command Number : ")
    try:
        query = int(query)
    except ValueError:
        print("Please Enter a Integer Value")
        main_dash()
    if query == 1:
        pass
    elif query == 2:
        pass
    elif query == 3:
        pass
    elif query == 4:
        pass
    else:
        print("Enter Correct Command Number")
        main_dash()

#Teacher Dashboard:
def teacher_dash():
    print("\n========================================\n" \
              "             TEACHER PANEL              \n" \
              "========================================\n\n" \
              "1. View Students\n" \
              "2. Search Student\n" \
              "3. Update Marks\n" \
              "4. Update Attendance\n" \
              "5. LogOut")
    query = input("Enter Command Number : ")
    try:
        query = int(query)
    except:
        print("\nPlease Enter a Valid Number")
        main_dash()
    if query == 1:
        pass
    elif query == 2:
        pass
    elif query == 3:
        pass
    elif query == 4:
        pass
    else:
        print("Enter Correct Command Number")
        main_dash()

#Admin Dashboard
def admin_dash():
    print("\n========================================\n" \
                  "             ADMIN PANEL              \n" \
                  "========================================\n\n" \
                  "1. View Students\n" \
                  "2. Search Student\n" \
                  "3. Update Marks\n" \
                  "4. Update Attendance\n" \
                  "5. Add New Student\n" \
                  "6. Remove Student\n" \
                  "7. Calculate Average Marks\n" \
                  "8. Calculate Average Attendance\n" \
                  "9. Change Password\n"\
                  "10. Logout")
    query = input("Enter Command Number : ")
    try:
         query = int(query)
    except:
            print("\nPlease Enter a Valid Number")
            admin_dash()
    if query == 1:
        pass
    elif query == 2:
        pass
    elif query == 3:
        pass
    elif query == 4:
        pass
    else:
        print("Enter Correct Command Number")
        main_dash()

main_dash()
db.close()