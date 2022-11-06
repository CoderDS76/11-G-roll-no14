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
    print("Marks must be out of 100!!")
    print("[1]To enter marks")
    print("[0]Exit the program")

menu()
choice=int(input("Enter your choice:-\t"))
sum=0
while choice!=0:
    n=int(input("Enter the number of subjects to update"))
    for n in range(1,n+1):
        sum+=int(input("Enter the marks:-\t"))
    else:
        Avg=sum/n
    break
Grade()