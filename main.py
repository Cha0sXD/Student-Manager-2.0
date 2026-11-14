# Importing Modules
import mysql.connector

# Connecting to SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Your Passsword",
    database = "Main")
cursor = db.cursor()

#Classes
class Person():
    def __init__(self,rank):
        self.rank = rank
    
    def finding_person(self,id):
        self.id = id
        query = None
        if self.rank == "s":
            query = """SELECT * from students WHERE id = %s"""
        elif self.rank == "t":
            query = """SELECT * from teachers WHERE teacher_id = %s"""
        values = (self.id,)
        cursor.execute(query,values)
        data = cursor.fetchone()
        if data == None:
            return None
        else:
            return data

    def exit():
        confirm = input("Confirm Exit y/n ?")
        if confirm == "y":
            return "y"
        elif confirm == "n":
            return "n"
        else:
            print("\nPlease Enter a Valid Value")
            return "a"

class Student():
    pass

class teacher():
    pass

class admin():
    pass

# Main Loop
count = True
while count == True:
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
        continue
    if query == 1:
        try:
            student_id = int(input("Enter Student ID : "))
            s1 = Person("s")
            data = s1.finding_person(student_id)
            if data == None:
                print("No Student Found")
                continue
            else:
                student_count = True
                print("\nWelcome ",data[1])
                while student_count == True:
                    print("\n========================================\n" \
                        "             STUDENT PANEL              \n" \
                        "========================================\n\n" \
                        "1. View Profle\n" \
                        "2. View Avergae Marks\n" \
                        "3. View Grades\n" \
                        "4. View Attendance\n" \
                        "5. LogOut")
                    query = input("Enter Command Number : ")
                    try:
                        query = int(query)
                    except ValueError:
                        print("\nPlease Enter a Valid Number")
                        continue
                    if query == 1:
                        print("Student ID - ",data[0],"\n",
                              "Name       - ",data[1],"\n",
                              "Course     - ",data[2],"\n",
                              "Semester   - ",data[3],"\n",
                              "Marks      - ",data[4],"\n",
                              "Attendance - ",data[5],"\n",
                              "Grade      - ",data[6],"\n")
                        continue
                    elif query == 2:
                        print("\nYour Average Marks are ",data[4],"%")
                        continue
                    elif query == 3:
                        print("\nYour Grades is ",data[6])
                    elif query == 4:
                        print("\nYour Attendance is ",data[5],"%")
                    elif query == 5:
                        pass
                    else:
                        print("Enter Correct Command Number")
                        continue
        except ValueError:
            print("Enter a Integer Value")
            continue


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