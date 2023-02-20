def menu():
    print("Pattern Printer!!")
    print()
    print("[1] Star Pattern")
    print("[2] Abc Pattern")
    print("[3] Number Pattern")
    print("[0] Exit")
    print()

#defining menu function
menu()
n=int(input("Choose any Pattern or Exit:    "))
while n!=0:
    if n==1:
        for i in range(1,6,2):
            print("*"*i)
        print()
        menu()
        n=int(input("Choose any Pattern or Exit:    "))
    elif n==2:    
        for j in range(1,5):
            for k in range(0,j):
                print(chr(65+k),end="")
            print()
        print()
        menu()
        n=int(input("Choose any Pattern or Exit:    "))
    elif n==3:
        for l in range(1,5):
            for m in range(1,5-l):
                print(" ",end=" ")
            for n in range(1,l+1):
                print(l,end=" ")
            print()
        print()
        menu()
        n=int(input("Choose any Pattern or Exit:    "))
    else:
        print("Invalid choice!!",end="\n\n")
        menu()
        n=int(input("Choose any Pattern or Exit:    "))
    #putting all conditions
print("Thank You For Using Pattern Printer!")
#End of code