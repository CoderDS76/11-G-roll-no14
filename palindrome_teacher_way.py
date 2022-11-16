num=int(input("Enter the number:-\t"))
n=num
rev=0
while n>0:
    dig=n%10
    rev=dig+(rev*10)
    n=n//10
if num==rev:
    print(num,"Is Palindrome")
else:
    print(num,"Is Not A Palindrom")