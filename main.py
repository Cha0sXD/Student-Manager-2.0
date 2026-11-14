# Importing Modules
import mysql.connector
from tabulate import tabulate

# Connecting to SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Doctor@10th",
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

    def view_student():
        query = """SELECT * from students"""
        cursor.execute(query)
        information = cursor.fetchall()
        head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
        print(tabulate(information, headers = head, tablefmt = "fancy_grid"))

    def update_stuff(self,what,id,new):
        if what == "m":
            query1 = """UPDATE students SET marks = %s WHERE id = %s"""
        elif what == "a":
            query1 = """UPDATE students SET attendance = %s WHERE id = %s"""
        values = (new,id)
        cursor.execute(query1,values)
        db.commit()
        print("\nSuccessfully Updated Data")

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
                        head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                        print(tabulate([data], headers = head, tablefmt = "fancy_grid"))
                        continue
                    elif query == 2:
                        print("\nYour Average Marks are ",data[4],"%")
                        continue
                    elif query == 3:
                        print("\nYour Grades is ",data[6])
                    elif query == 4:
                        print("\nYour Attendance is ",data[5],"%")
                    elif query == 5:
                        confirm = input("Confirm Exit y/n ? ")
                        if confirm == "y":
                            student_count = False
                        elif confirm == "n":
                            continue
                        else:
                            print("\nPlease Enter a Valid Value")
                            continue
                    else:
                        print("Enter Correct Command Number")
                        continue
        except ValueError:
            print("Enter a Integer Value")
            continue

    elif query == 2:
        try:
            teacher_id = int(input("Enter Teacher ID : "))
            t1 = Person("t")
            data2 = t1.finding_person(teacher_id)
            if data2 == None:
                print("No Teacher Found")
                continue
            else:
                teacher_count = True
                print("\nWelcome ",data2[1])
                while teacher_count == True:
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
                    except ValueError:
                        print("\nPlease Enter a Valid Number")
                        continue
                    if query == 1:
                        Person.view_student()
                        continue
                    elif query == 2:
                        search_id = input("Enter Student ID : ")
                        try:
                            search_id = int(search_id)
                        except ValueError:
                            print("Enter a Valid ID")
                            continue
                        s2 = Person("s")
                        data3 = s2.finding_person(search_id)
                        if data3 == None:
                            print("No Studnet Found")
                            continue
                        else:
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([data3], headers = head, tablefmt = "fancy_grid"))
                            continue

                    elif query == 3:
                        mark_id = input("Enter Student ID : ")
                        try:
                            mark_id = int(mark_id)
                        except:
                            print("Please Enter Integer Value")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(mark_id)
                        if found == None:
                            print("No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt= "fancy_grid"))
                            new_data = input("Enter New Marks Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print("Enter Integer Value")
                                continue
                        u1.update_stuff("m",mark_id,new_data)
                        continue

                    elif query == 4:
                        update_id = input("Enter Student ID - ")
                        try:
                            update_id = int(update_id)
                        except:
                            print("Enter Valid ID")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(update_id)
                        if found == None:
                            print("No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt = "fancy_grid"))
                            new_data = input("Enter New Attendance Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print("Enter Integer Value")
                                continue
                        u1.update_stuff("a",update_id,new_data)
                        continue

                    elif query == 5:
                        confirm = input("Are you Sure? y/n : ")
                        if confirm == "y":
                            teacher_count = False
                        elif confirm == "n":
                            continue
                        else:
                            print("Enter a Valid Value")
                    else:
                        print("Enter Correct Command Number")
                        continue
        except ValueError:
            print("Enter a Integer Value")
            continue

db.close()