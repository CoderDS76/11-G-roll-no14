def menu():
    print("String Stuff")
    print()
    print("[1] Find length of String")
    print("[2] Copy a String")
    print("[3] Concat two Strings")
    print("[4] Compare two Strings")
    print("[5] Reverse a String")
    print("[6] Check if String is a Pallindrome")
    print("[0] Exit")
    print()

#Defining Menu
menu()
n=int(input("Enter your choice:    "))
print()
while n!=0:
    if n==1:
        s=input("Enter the String:   ")
        print("The length of the String is: ",len(s))
        print()
    elif n==2:
        t=input("Enter the String:   ")
        v=str(t)
        print("The copy of the string",t,"is",v)
        print()
    elif n==3:
        c1=input("Enter the First String:   ")
        c2=input("Enter the Second String:   ")
        print("The concat is: ",(c1+c2))
        print()
    elif n==4:
        sen1=input("Enter the first strings:  ")
        sen2=input("Enter the second string:  ")
        if sen1==sen2:
            print("The strings are EQUAL!")
        else:
            print("The strings are NOT EQUAL!")
        print()
    elif n==5:
        l=input("Enter the String:    ")
        print("The reverse of",l,"is",(l[::-1]))
        print()
    elif n==6:
        pal=input("Enter the String:    ")
        if pal==pal[::-1]:
            print("The string is a PALLINDROME!!")
        else:
            print("The string is NOT a PALLINDROME")
        print()
    else:
        print("Invalid Choice!!")
        print()
    menu()
    n=int(input("Enter your choice:    "))
    #All Conditions
print("Thank You For Using String Stuff!!")
#End of Code