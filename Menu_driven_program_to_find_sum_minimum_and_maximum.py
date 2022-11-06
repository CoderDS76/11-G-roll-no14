def menu():
    print("Select one of the options given below")
    print("[1]Find the sum of given numbers")
    print("[2]Find the minimum of given numbers")
    print("[3]Find the maximum of given numbers")
    print("[0]Exit the Program")

menu()
choice=int(input("Enter your choice:-\t"))
while choice!=0:
    if choice== 1 :
        num=int(input("Enter the number of terms:-\t"))
        sum=0
        list1=[]
        for i in range(0,num):
            terms=int(input("Enter the number:-\t"))

            list1.append(terms)
        for j in list1:
            sum+=j
        print("\n The sum of the given numbers is:-\t",sum,"\n")
    elif choice== 2 :
        num=int(input("Enter the number of terms:-\t"))
        list2=[]
        for i in range(0,num):
            elements=int(input("Enter the number:-\t"))

            list2.append(elements)
        print("\n The lowest number given is:-\t",min(list2),"\n")
    elif choice== 3 :
        num=int(input("Enter the number of terms:-\t"))
        list3=[]
        for i in range(0,num):
                elements=int(input("Enter the number:-\t"))

                list3.append(elements)
        print("\n The highest number given is:-\t",max(list3),"\n")
    else:
        print("Wrong choice!!\n")
    menu()
    choice=int(input("Enter your choice:-\t"))

print("Thanks for using this program!!")