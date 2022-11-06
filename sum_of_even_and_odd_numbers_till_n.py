n=int(input("Enter the number:-\t"))        #Taking number from user
sum1=0
sum2=0
#Declaring variable(sum)
for i in range(1,n+1):
    if i%2==0:
        sum1+=i
    else:
        i+=1
#if else within for loop, for i in range 1,n+1 and if i is even then, sum=sum+i else, assign i=i+1 
for j in range(1,n+1):
    if j%2!=0:
        sum2+=j
    else:
        j+=1
#if else within for loop, for j in range 1,n+1 and if j is odd then, sum = sum+j else, assign j = j+1 
print("The sum of even numbers till",n,"is:-\t",sum1)
print("The sum of odd numbers till",n,"is:-\t",sum2)
#printing the sum