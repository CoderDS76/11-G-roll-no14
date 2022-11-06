num=int(input("Enter a Number(positive):-\t"))  #Taking number from user
i=1
factorial=1
#Declaring variables(i and factorial)
while i<=num:
    factorial*=i
    i+=1
#while loop condition, while i is less than num then keep multiplying factorial by i and assign i=i+1
print("The factorial of",num,"is:-\t",factorial)
#printing the factorial