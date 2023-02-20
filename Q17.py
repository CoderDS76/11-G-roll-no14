def menu():
    print("Alphabet And Case Checker")
    print()
    print("[1] Check if in Alphabet and if alphabet check case")
    print("[0] Exit")
    print()

#Definig Menu
menu()
n=int(input("Enter your choice:    "))
while n!=0:
    if n==1:
        print()
        x=input("Enter the character:  ")
        if x.isalpha():
            print("Yes",x,"is in the alphabet")
            if x.islower():
                print("It is in LOWERCASE!")
            else:
                print("It is in UPPERCASE!")
        else:
            print(x,"is not in the aplhabet")
        print()
    else:
        print("Invalid Choice!!")
        print()
    menu()
    n=int(input("Enter your choice:    "))
    #All Conditions
print("Thank You For Using Char Checker!")
#End of code