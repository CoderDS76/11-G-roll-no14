def menu():
    print()
    print("List Element Searcher (LES)")
    print("[1] Find Element")
    print("[0] Exit")
    print()

#Defining menu
menu()
n=int(input("Enter your choice:   "))
print()
while n!=0:
    if n==1:
        print()
        terms=input("Enter the terms seperated by 2 spaces:  ")
        print()
        term=input("Enter the term to search for:  ")
        if term in terms.split():
            print("The term is in the list")
        else:
            print("Term NOT FOUND!!")
    else:
        print("INVALID CHOICE!!")
    menu()
    n=int(input("Enter your choice:   "))
    #All Conditions
print("Thank You For Using LES")
#End of Code