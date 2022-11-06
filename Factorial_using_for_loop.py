num=int(input("Enter a number(positive):-\t"))  #Taking number from user
factorial=1     #Declaring a variable(factorial)
for i in range(1,num+1):
    factorial*=i
#for loop condition:- if i is in range 1, num+1 then, keep multiplying factorial by i(i changes value as per the range)
print("The factorial of",num,"is:-\t",factorial)
#printing the factorial