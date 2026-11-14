# Importing Modules
import mysql.connector
from tabulate import tabulate
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Connecting to SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Doctor@10th",
    database = "Main")
cursor = db.cursor()

#Classes
class Person():
    password = "admin123"
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
        if data is None:
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
    def __init__(self,rank):
        self.rank = rank

    def add(self):
        if self.rank == "s":
            command = """INSERT INTO students (name, course, semester, marks, attendance, grade)
                        VALUES(%s,%s,%s,%s,%s,%s)
                        """
            name = input(Fore.BLUE + "Enter Student Name : ")
            course = input(Fore.BLUE + "Enter Course : ")
            semester = input(Fore.BLUE + "Enter Semester : ")
            marks = input(Fore.BLUE + "Enter Marks : ")
            attendance = input(Fore.BLUE + "Enter Attendance : ")
            grade = input(Fore.BLUE + "Enter Grade : ")
            grade = grade.capitalize()
            valid = True
            try:
                semester = int(semester)
                marks = int(marks)
                attendance = int(attendance)
                if semester <1  or semester > 8:
                    print(Fore.RED + "Semester Must be Between 1-8")
                    valid = False
                if marks > 100 or marks < 0:
                    print("Marks must be between 0-100")
                    valid = False
                if attendance > 100 or attendance < 0:
                    print("Attendance must be between 0-100")
                    valid = False
                if grade not in ("A","A+","B","C","D","E","F"):
                    print(Fore.RED + "Grade must be A, A+, B, C, D, E or F")
                    valid = False
                if valid is True:
                    values = (name,course,semester,marks,attendance,grade)
                    cursor.execute(command,values)
                    db.commit()
                    print(Fore.GREEN + "New Student Added")
            except ValueError:
                print("Please Enter Valid Values")

        elif self.rank == "t":
            command = """INSERT INTO teachers (teacher_name)
                        VALUES(%s)
                      """
            teacher_name = input("Enter Teacher Name : ")
            values = (teacher_name,)
            cursor.execute(command,values)
            db.commit()

    def remove(self):
        if self.rank == "s":
            command = """DELETE FROM students WHERE id = %s"""
            remove_id = input("Enter Student ID : ")
            try:
                remove_id = int(remove_id)
            except ValueError:
                print(Fore.RED + "Enter a Integer Value")
                return
            s3 = Person("s")
            remove = s3.finding_person(remove_id)
            if remove is None:
                print(Fore.RED + "No Student Found")
            else:
                head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                print(tabulate([remove],headers = head, tablefmt = "fancy_grid"))
                confirm = input("Are you sure, you wanna go ahead? y/n : ")
                if confirm == "y":
                    value = (remove_id,)
                    cursor.execute(command,value)
                    db.commit()
                    print("Student Removed Successfully")
                elif confirm == "n":
                    return
                else:
                    print(Fore.RED + "Enter Valid Value")
                    return
                
        elif self.rank == "t":
            command = """DELETE FROM teachers WHERE teacher_id = %s"""
            remove_id = input("Enter Teacher ID : ")
            try:
                remove_id = int(remove_id)
            except ValueError:
                print(Fore.RED + "Enter a Integer Value")
                return
            t3 = Person("t")
            remove = t3.finding_person(remove_id)
            if remove is None:
                print(Fore.RED + "No Teacher Found")
            else:
                head = ["ID","Teacher Name"]
                print(tabulate([remove],headers = head, tablefmt = "fancy_grid"))
                confirm = input("Are you sure, you wanna go ahead? y/n : ")
                if confirm == "y":
                    value = (remove_id,)
                    cursor.execute(command,value)
                    db.commit()
                    print("Teacher Removed Successfully")
                elif confirm == "n":
                    return
                else:
                    print(Fore.RED + "Enter Valid Value")
                    return

    def average(what):
        command1 = """SELECT COUNT(id) from students"""
        cursor.execute(command1)
        total = cursor.fetchone()[0]
        if what == "m":
            command = """SELECT AVG(marks) from students;"""
            cursor.execute(command)
            average_marks = cursor.fetchone()[0]
            print(f"Average Marks of {total} Students is {average_marks:.2f}%")
            return
        elif what == "a":
            command = """SELECT AVG(attendance) from students;"""
            cursor.execute(command)
            average_attendance = cursor.fetchone()[0]
            print(f"Average Attendance of {total} students is {average_attendance:.2f}%")
        
# Main Loop
count = True
while count == True:
    print(Fore.YELLOW + "========================================\n" \
          "             STUDENT MANAGER              \n" \
          "========================================\n\n" \
          "1. Student Login\n" \
          "2. Teacher Login\n" \
          "3. Admin Login\n" \
          "4. Exit\n")
    query = input(Fore.CYAN + "Enter The Command Number : ")
    try:
        query = int(query)
    except ValueError:
        print(Fore.RED + "Please Enter a Integer Value")
        continue
    if query == 1:
        try:
            student_id = int(input("Enter Student ID : "))
            s1 = Person("s")
            data = s1.finding_person(student_id)
            if data is None:
                print(Fore.RED + "No Student Found")
                continue
            else:
                student_count = True
                print(Fore.BLUE + "\nWelcome "+data[1])
                while student_count == True:
                    print(Fore.YELLOW + "========================================\n" \
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
                            print(Fore.RED + "\nPlease Enter a Valid Value")
                            continue
                    else:
                        print(Fore.RED + "Enter Correct Command Number")
                        continue
        except ValueError:
            print(Fore.RED + "Enter a Integer Value")
            continue

    elif query == 2:
        try:
            teacher_id = int(input("Enter Teacher ID : "))
        except ValueError:
            print(Fore.RED + "Enter a Integer Value")
            continue
        teacher_count = True
        while teacher_count is True:
                    t1 = Person("t")
                    data2 = t1.finding_person(teacher_id)
                    if data2 is None:
                        print(Fore.RED + "No Teacher Found")
                        teacher_count = False
                        break
                    else:
                        teacher_count = True
                        print(Fore.BLUE + "\nWelcome "+data2[1])

                    print(Fore.YELLOW + "========================================\n" \
                            "             TEACHER PANEL              \n" \
                            "========================================\n\n" \
                            "1. View Students\n" \
                            "2. Search Student\n" \
                            "3. Update Marks\n" \
                            "4. Update Attendance\n" \
                            "5. LogOut")
                    query = input(Fore.CYAN + "Enter Command Number : ")
                    try:
                        query = int(query)
                    except ValueError:
                        print(Fore.RED + "\nPlease Enter a Valid Number")
                        continue
                    if query == 1:
                        Person.view_student()
                        continue
                    elif query == 2:
                        search_id = input("Enter Student ID : ")
                        try:
                            search_id = int(search_id)
                        except ValueError:
                            print(Fore.RED + "Enter a Valid ID")
                            continue
                        s2 = Person("s")
                        data3 = s2.finding_person(search_id)
                        if data3 is None:
                            print(Fore.RED + "No Studnet Found")
                            continue
                        else:
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([data3], headers = head, tablefmt = "fancy_grid"))
                            continue
                    elif query == 3:
                        mark_id = input("Enter Student ID : ")
                        try:
                            mark_id = int(mark_id)
                        except ValueError:
                            print(Fore.RED + "Please Enter Integer Value")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(mark_id)
                        if found is None:
                            print(Fore.RED + "No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt= "fancy_grid"))
                            new_data = input("Enter New Marks Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print(Fore.RED + "Enter Integer Value")
                                continue
                        if 0 <=new_data <= 100:
                            u1.update_stuff("m",mark_id,new_data)
                            continue
                        else:
                            print("Marks Should be Between 0-100")
                            continue
                    elif query == 4:
                        update_id = input("Enter Student ID - ")
                        try:
                            update_id = int(update_id)
                        except ValueError:
                            print(Fore.RED + "Enter Valid ID")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(update_id)
                        if found is None:
                            print(Fore.RED + "No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt = "fancy_grid"))
                            new_data = input("Enter New Attendance Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print(Fore.RED + "Enter Integer Value")
                                continue
                        if 0 <=new_data <= 100:
                            u1.update_stuff("a",update_id,new_data)
                            continue
                        else:
                            print(Fore.RED + "Attendance Should be Between 0-100")
                            continue
                    elif query == 5:
                        confirm = input("Are you Sure? y/n : ")
                        if confirm == "y":
                            teacher_count = False
                        elif confirm == "n":
                            continue
                        else:
                            print(Fore.RED + "Enter a Valid Value")
                    else:
                        print(Fore.RED + "Enter Correct Command Number")
                        continue

    elif query == 3:
        password = input("Enter Password : ")
        if password == Person.password:
            admin_count = True
            print(Fore.BLUE + "\nWelcome Admin")
            while admin_count == True:
                print(Fore.YELLOW + "========================================\n" \
                                "             ADMIN PANEL              \n" \
                              "========================================\n\n" \
                              "1. View Students\n" \
                              "2. Search Student\n" \
                              "3. Update Marks\n" \
                              "4. Update Attendance\n" \
                              "5. Add New Student\n" \
                              "6. Remove Student\n" \
                              "7. Add New Teacher\n"\
                              "8. Remove Teacher\n"\
                              "9. Calculate Average Marks\n" \
                              "10. Calculate Average Attendance\n" \
                              "11. Change Password\n"\
                              "12. Logout")
                query = input(Fore.CYAN + "\nEnter Command Number : ")
                try:
                    query = int(query)
                except ValueError:
                    print(Fore.RED + "\nEnter Numerical Value")
                    continue
                if query == 1:
                        Person.view_student()
                        continue
                elif query == 2:
                        search_id = input("Enter Student ID : ")
                        try:
                            search_id = int(search_id)
                        except ValueError:
                            print(Fore.RED + "Enter a Valid ID")
                            continue
                        s2 = Person("s")
                        data3 = s2.finding_person(search_id)
                        if data3 is None:
                            print(Fore.RED + "No Studnet Found")
                            continue
                        else:
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([data3], headers = head, tablefmt = "fancy_grid"))
                            continue
                elif query == 3:
                        mark_id = input("Enter Student ID : ")
                        try:
                            mark_id = int(mark_id)
                        except ValueError:
                            print(Fore.RED + "Please Enter Integer Value")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(mark_id)
                        if found is None:
                            print(Fore.RED + "No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt= "fancy_grid"))
                            new_data = input("Enter New Marks Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print(Fore.RED + "Enter Integer Value")
                                continue
                        if 0 <=new_data <= 100:
                            u1.update_stuff("m",mark_id,new_data)
                            continue
                        else:
                            print("Marks Should be Between 0-100")
                            continue
                elif query == 4:
                        update_id = input("Enter Student ID - ")
                        try:
                            update_id = int(update_id)
                        except ValueError:
                            print(Fore.RED + "Enter Valid ID")
                            continue
                        u1 = Person("s")
                        found = u1.finding_person(update_id)
                        if found is None:
                            print(Fore.RED + "No Student Found")
                            continue
                        else:
                            print("Student Found")
                            head = ["ID","Name","Course","Semester","Marks","Attendance","Grade"]
                            print(tabulate([found], headers = head, tablefmt = "fancy_grid"))
                            new_data = input("Enter New Attendance Data : ")
                            try:
                                new_data = int(new_data)
                            except ValueError:
                                print(Fore.RED + "Enter Integer Value")
                                continue
                        if 0 <=new_data <= 100:
                            u1.update_stuff("a",update_id,new_data)
                            continue
                        else:
                            print(Fore.RED + "Attendance Should be Between 0-100")
                            continue
                elif query == 5:
                    a1 = admin("s")
                    a1.add()
                elif query == 6:
                    a2 = admin("s")
                    a2.add()
                    admin.remove()
                elif query == 7:
                    t2 = admin("t")
                    t2.remove()
                elif query == 8:
                    t3 = admin("t")
                    t3.remove()
                elif query == 9:
                    admin.average("m")
                elif query == 10:
                    admin.average("a")
                elif query == 11:
                    current = input(Fore.BLUE + "Enter Current Password : ")
                    if current == Person.password:
                        new = input(Fore.BLUE + "Enter New Password : ")
                        Person.password = new
                        print(Fore.GREEN + "Password Changed")
                    else:
                        print(Fore.RED + "Wrong Password")
                        continue
                elif query == 12:
                    confirm = input("Are You sure? y/n : ")
                    if confirm == "y":
                        print(Fore.RED + "Exiting...")
                        admin_count = False
                    elif confirm == "n":
                        continue
                    else:
                        print(Fore.RED + "Enter Valid command")
                        continue
        else:
            print("\nWrong Password")
            continue

db.close()