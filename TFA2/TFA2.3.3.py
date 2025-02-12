lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = input("Enter age: ")
contact = input("Enter contact number: ")
course = input("Enter course: ")

studentinfo = ["Last Name: ", lname, "\nFirst Name: ", fname, "\nAge: ", age, "\nContact Number: ", contact,
               "\nCourse: ", course]
f=open("students.txt","a")
f.writelines(studentinfo)
f.close()

print("Student information has been save to 'students.txt.'" )

