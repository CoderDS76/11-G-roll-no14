def menu():
    print()
    print("LIST STUFF")
    print("[1] Print Reverse")
    print("[2] Find Sum of Elements")
    print("[3] Find Average of list")
    print("[4] Find Standard Deviation")
    print("[0] Exit")
    print()

#Defining Menu
menu()
n=int(input("Enter your choice:  "))
print()
while n!=0:
    if n==1:
        terms=input("Enter the terms seperated by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        print("The reverse of the list is:  ",l[::-1])
    elif n==2:
        terms=input("Enter the terms seperated by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        sum=0
        for j in l:
            sum+=j
        print("The sum of the elements is:  ",sum)
    elif n==3:
        terms=input("Enter the terms seperated by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        sum=0
        for j in l:
            sum+=j
        mean=(sum/len(l))
        print("The average of the list is:  ",mean)
    elif n==4:
        terms=input("Enter the terms seperated by 2 spaces:  ")
        l=[]
        for term in terms.split():
            l.append(int(term))
        sum=0
        for j in l:
            sum+=j
        sd=0
        mean=(sum/len(l))
        for i in l:
            sd+=((i-mean)**2)/len(l)
        print("The Standard Deviation of the list is:  ",sd)
    else:
        print("INVALID CHOICE!!")
    menu()
    n=int(input("Enter your choice:  "))
    #All Conditions
print("Thank You For Using LIST STUFF")
#End of Code