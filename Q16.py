def menu():
    print("Armstrong, Prime, Pallindrome Checker!!")
    print()
    print("[1] Check if Armstrong")
    print("[2] Check if Prime")
    print("[3] Check if Pallindrome")
    print("[0] Exit")
    print()

#Defing menu
menu()
k=int(input("Enter your choice:    "))
while k!=0:
    if k==1:
        n=int(input("Enter the number to be checked:  "))
        sum=0
        temp=n
        nodig=len(str(temp))
        while temp>0:
            i=temp%10
            sum+=(i**nodig)
            temp//=10
        if sum==n:
            print("The Number",n,"is ARMSTRONG!!")
        else:
            print("The Number",n,"is NOT ARMSTRONG!!")
        print()
        menu()
        k=int(input("Enter your choice:    "))
    elif k==2:
        n=int(input("Enter the number to be checked:  "))
        if n>1:
            for i in range(2,int(n/2)+1):
                if n%i==0:
                    print("The Number",n,"is NOT PRIME")
                    break
            else:
                print("The Number",n,"is PRIME")
        else:
            print("The Number",n,"is not prime")
        print()
        menu()
        k=int(input("Enter your choice:    "))
    elif k==3:
        n=int(input("Enter the number to be checked:  "))
        m=str(n)
        rev=m[::-1]
        if m==rev:
            print("The Number",n,"is a PALLINDROME")
        else:
            print("The Number",n,"is NOT a PALLINDROME")
        print()
        menu()
        k=int(input("Enter your choice:    "))
    else:
        print("Invalid Choice!!")
        print()
        menu()
        k=int(input("Enter your choice:    "))
    #All conditions
print("Thank You For Using APP Checker")
#End of Code