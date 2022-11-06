def Grade():
                if Avg>86:
                    print("Grade:- A")
                elif Avg<86 and Avg>72:
                    print("Grade:- B")
                elif Avg<72 and Avg>58:
                    print("Grade:- C")
                elif Avg<58 and Avg>44:
                    print("Grade:- D")
                elif Avg<44 and Avg>30:
                    print("Grade:- E")
                else: 
                    print("Grade:- F")
def menu():
    print("Student Grader")
    print("Marks must be out of 100 and must be entered in order")
    print("[1]Enter marks of first subject")
    print("[2]Enter marks of second subject")
    print("[3]Enter marks of third subject")
    print("[4]Enter marks of fourth subject")
    print("[5]Enter marks of fifth subject")
    print("[6]Show Grade of student")
    print("[0]Exit the program")

menu()
choice=int(input("Enter your choice:-\t"))
while choice !=0:
    if choice==1:
        sub1=int(input("Enter the marks of Subject 1:-\t"))
        menu()
        choice=int(input("Enter your choice:-\t"))
    elif choice==2:
        sub2=int(input("Enter the marks of Subject 2:-\t"))
        menu()
        choice=int(input("Enter your choice:-\t"))
    elif choice==3:
        sub3=int(input("Enter the marks of Subject 3:-\t"))
        menu()
        choice=int(input("Enter your choice:-\t"))
    elif choice==4:
        sub4=int(input("Enter the marks of Subject 4:-\t"))
        menu()
        choice=int(input("Enter your choice:-\t"))
    elif choice==5:
        sub5=int(input("Enter the marks of Subject 5:-\t"))
        menu()
        choice=int(input("Enter your choice:-\t"))
    elif choice==6:
        n=int(input("Enter the number of subjects updated:-\t"))
        if n==1:
            Avg=sub1
            Grade()
        elif n==2:
            Avg=(sub1+sub2)/n
            Grade()
            
        elif n==3:
            Avg=(sub1+sub2+sub3)/n
            Grade()
            
        elif n==4:
            Avg=(sub1+sub2+sub3+sub4)/n
            Grade()
            
        elif n==5:
            Avg=(sub1+sub2+sub3+sub4+sub5)/n
            Grade()
            
        else:
            print("Wrong input!!")
        menu()
        choice=int(input("Enter your choice:-\t"))
    else:
        print("Wrong input!!")
        menu()
print("Thank you for using Student Grader!!")