def menu():
    print()
    print("MAX and MIN of a LIST")
    print()
    print("[1] Find MAX VALUE")
    print("[2] Find MIN VALUE")
    print("[0] Exit")
    print()

#Defining menu
menu()
n=int(input("Enter your choice:   "))
while n!=0:
    if n==1:
        print()
        terms=input("Enter the numbers separeted by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        print("The MAX VALUE in this list is:  ", max(l))
    elif n==2:
        print()
        terms=input("Enter the numbers separeted by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        print("The MIN VALUE in this list is:  ",min(l))

    else:
        print()
        print("INVALID CHOICE!!")
    menu()
    n=int(input("Enter your choice:   "))
    #All Conditions
print("Thank You For Using Max and Min of a LIST")
#End of Code