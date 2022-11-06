num1=float(input("Enter the First number:-\t"))
num2=float(input("Enter the Second number:-\t"))
num3=float(input("Enter the Third number:-\t"))
#Taking 3 Numbers from user
if num1<num2 and num1<num3:
    print("The smallest number is:-\t",num1)
elif num2<num1 and num2<num3:
    print("The smallest number is:-\t",num2)
else:
    print("The smallest number is:-\t",num3)
#Finding and Printing the smallest number