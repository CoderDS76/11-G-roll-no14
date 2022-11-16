n=int(input("Enter the number of times to iterate:\t"))
num1=0
num2=1
num=0
print(num1,num2,end=" ")
for i in range(1,n+1):
    num=num1+num2
    print(num,end=" ")
    num1=num2
    num2=num