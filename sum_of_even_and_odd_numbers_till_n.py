n=int(input("Enter the number:-\t"))        #Taking number from user
sum1=0
sum2=0
#Declaring variable(sum)
for i in range(1,n+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
#if else within for loop, for i in range 1,n+1 and if i is even then, sum1=sum1+i else, i is odd, sum2=sum2+i
print("The sum of even numbers till",n,"is:-\t",sum1)
print("The sum of odd numbers till",n,"is:-\t",sum2)
#printing the sum