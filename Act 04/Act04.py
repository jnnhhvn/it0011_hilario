file = "records.txt"
records = []

while True:
    print("\n==============MENU==============\n")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    
    choice = input("\nEnter choice: ")

    if choice == "1":
        try:
            with open(file, "r") as f:
                records = [eval(line.strip()) for line in f]
            print("Records successfully loaded.")
        except FileNotFoundError:
            print("No records found.")
            
    elif choice == "2":
        with open(file, "w") as f:
            for record in records:
                f.write(str(record) + "\n")
        print("Records saved.")

    elif choice == "3":
        file = input("Enter new filename: ")
        with open(file, "w") as f:
            for record in records:
                f.write(str(record) + "\n")
        print("Records saved as", file)

    elif choice == "4":
        sort_option = input("Sort by (1) Last Name or (2) Grade? ")
        if sort_option == "1":
            records.sort(key=lambda x: x[1][1])
        elif sort_option == "2":
            records.sort(key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
        else:
            print("Invalid choice.")
            continue

        print("\n========= Student Records =========")
        for record in records:
            total_grade = record[2] * 0.6 + record[3] * 0.4
            print(f"Student ID: {record[0]}")
            print(f"First Name: {record[1][0]}")
            print(f"Last Name: {record[1][1]}")
            print(f"Class Standing: {record[2]}")
            print(f"Major Exam Grade: {record[3]}")
            print(f"Total Grade: {total_grade:.2f}")
            print("----------------------------------")

    elif choice == "5":
        id_num = input("Enter Student ID: ")
        for record in records:
            if record[0] == id_num:
                total_grade = record[2] * 0.6 + record[3] * 0.4
                print("\n========= Student Record =========")
                print(f"Student ID: {record[0]}")
                print(f"First Name: {record[1][0]}")
                print(f"Last Name: {record[1][1]}")
                print(f"Class Standing: {record[2]}")
                print(f"Major Exam Grade: {record[3]}")
                print(f"Total Grade: {total_grade:.2f}")
                print("----------------------------------")
                break
        else:
            print("Student not found.")

    elif choice == "6":
        id_num = input("Enter Student ID (8 digits): ")
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        standing = float(input("Enter Class Standing Grade: "))
        exam = float(input("Enter Major Exam Grade: "))
        records.append((id_num, (fname, lname), standing, exam))
        print("Record added.")

    elif choice == "7":
        id_num = input("Enter Student ID to update: ")
        for i, record in enumerate(records):
            if record[0] == id_num:
                fname = input("Enter New First Name: ")
                lname = input("Enter New Last Name: ")
                standing = float(input("Enter New Class Standing Grade: "))
                exam = float(input("Enter New Major Exam Grade: "))
                records[i] = (id_num, (fname, lname), standing, exam)
                print("Record updated.")
                break
        else:
            print("Student not found.")

    elif choice == "8":
        id_num = input("Enter Student ID to delete: ")
        records[:] = [record for record in records if record[0] != id_num]
        print("Record deleted.")

    elif choice == "9":
        break

    else:
        print("Invalid choice. Please try again.")