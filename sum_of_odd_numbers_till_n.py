n=int(input("Enter the number:-\t"))        #Taking number from user
sum=0
#Declaring variable(sum)
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
    else:
        i+=1
#if else within for loop, for i in range 1,n+1 and if i is odd then, sum=sum+i else, assign i=i+1 
print("The sum of odd numbers till",n,"is:-\t",sum)
#printing the sum