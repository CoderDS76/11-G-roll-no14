def menu():
    print("Fibonacci Printer!!")
    print()
    print("[1]Choose number of terms")
    print("[0]Exit")
#defining menu
menu()
print()
n=int(input("Enter 0 or 1:    "))
while n!=0:
    r=int(input("Enter the number of times to iterate:\t"))
    num1=0
    num2=1
    num=0
    if r>2:
        print(num1,num2,end=" ")
        for i in range(1,r-1):
            num=num1+num2
            print(num,end=" ")
            num1=num2
            num2=num
        print()
    elif r==2:
        print(num1,num2)
    else:
        print(num1)
    print()
    menu()
    print()
    n=int(input("Enter 0 or 1:    "))
    #All conditions
print("Thank You For Using Fibonacci Printer!")
#End of code