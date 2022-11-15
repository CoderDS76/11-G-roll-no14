def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
sum=0
number=int(input("Enter the base number for the series:-\t"))
times=int(input("Enter the number of times to sum the series for:-\t"))
for i in range(1,times+1):
    sum=sum+(number**i)/fact(i)
print(sum,"Is The Sum Of the Series (x^n)/n! For",times,"Times")