import json
try:
    with open ("students.json","r") as file:
        students = json.load(file)

except FileNotFoundError:
    print("File Does Not Exist.!")
    students = []

except json.JSONDecodeError:
    print("Invalid Json File !")
    students = []


while  True:

    print("====================================")
    print("=========== WELCOME ============")
    print(" STUDENT RECORD MANAGEMENT SYSTEM ")
    print(" MANAGE YOUR STUDENTS RECORD EASILY ")
    print("====================================")

    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Student Count")
    print("7. Exit")

    try:

        choice = int(input("Enter Your Choice :"))

    except ValueError:
        print("Please Enter Numbers Only !")
        continue

    if choice == 7:
        print("=====================================")
        print("Thank You For Using Our Application...!")
        print("All Students Records Have Been Saved")
        print("=====================================")
        break
        

    elif choice == 1:
        print("Add Student Selected .")

        try:

            student_id = int(input("Enter Student ID :"))
            
        except ValueError:
            print("Invalid Student ID! Please Enter Numbers Only !")
            continue

        if student_id <= 0:
            print("Student ID Must Be Greater Than Zero !")
            continue

        for student in students:
            if student["id"] == student_id:
                print("Student ID Is Already Exist.!")
                break

        else:
            print("Student ID Is Unique.!")

        

            name = input("Enter Student Name :").strip()
            if not name:
                print("Invalid Input! Enter Letters Only !")
                continue

            try:
                age = int(input("Enter Student Age :"))

            except ValueError:
                print("Invalid Age! Please Enter Numbers Only!")
                continue
            if age <= 0:
                print("Age Must Be Greater Than Zero!")
                continue

            course = input("Enter Student Course :").strip()
            if not course:
                print("Course Cannot Be Empty !")
                break

            student = {
                "id" : student_id,
                "name" : name,
                "age" : age,
                "course" : course
            }

        # print("Student Details :",student)
            students.append(student)

            with open("students.json", "w") as file:
                json.dump(students,file,indent=4)

            print("Student Data Added Successfully !")

    elif choice == 2:
        print("View All Student Selected .")

        

        if not students:
            print("Students Record Not Found!")

        else:    
            for student in students:
                print("--------------------------")
                print("ID:", student["id"])
                print("NAME:", student["name"])
                print("AGE:", student["age"])
                print("COURSE:", student["course"])
                print("--------------------------")

    elif choice == 3:
        print("Search Student Selected .")

        
        try:
            
            search_id = int(input("Enter Student_Id to Search :"))
            
        except ValueError:
            print("Enter Valid ID !")
            continue

        found = False

        for student in students:
            if student["id"] == search_id:
                print("Student Found")
                print("Your Search Student Data Is Here :")
                print("--------------------------")
                print("ID:", student["id"])
                print("NAME:", student["name"])
                print("AGE:", student["age"])
                print("COURSE:", student["course"])
                print("--------------------------")
                print()

                
                found = True
                break

        if not found:
            print("Student Not Found!")

                
    elif choice == 4:
        print("Update Student Selected .")

        try:

            update_id = int(input("Enter Student ID to Update : "))
            

        except ValueError:
            print("Enter Valid ID !")
            continue

        found = False

        for student in students:
            if student["id"] == update_id:
                print("Student Found!")

                print("Enter The New Student Details :")
                new_name = input("Enter New Name:").strip()
                if not new_name:
                    print("Name Cannot Be Empty !")
                    break


                try:
                    new_age = int(input("Enter New Age:"))

                except ValueError:
                    print("Enter Valid Age !")
                    continue

                if new_age <= 0:
                    print("Age Must Be Greater Than Zero !")
                    break

                new_course = input("Enter New Course:").strip()
                if not new_course:
                    print("Student Course Cannot Be Empty!")
                    break

                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course

                with open("students.json","w") as file:
                    json.dump(students,file,indent=4)

                print("Student Data Update Successfully !")
                found = True
                break

        if not found:
            print("Student Not Found!")        

    elif choice == 5:
        print("Delete Student Selected .")

        found = False
        try:

            delete_id = int(input("Enter The ID To Delete :"))
            found = False

        except ValueError:
            print("Enter Valid ID !")
            continue

        for student in students:
            if student["id"] == delete_id:
                print("Student Found !")

                students.remove(student)

                with open("students.json","w") as file:
                    json.dump(students,file,indent=4)

                print("Student Data Delete Successfully !")

                found = True
                break

        if not found:
            print("Student Not Found!") 

    elif choice == 6:
        print("Total Student Count Selected .")
        print("---------------------------------")
        print("Total Register Student :",len(students))
        print(f"You Have Total {len(students)} Students in The Data")
        print("---------------------------------")
        

    else:
        print("Invalid Choice .")


