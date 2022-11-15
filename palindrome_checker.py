x=input("Enter the string or number (THIS PROGRAM IS CASE SENSITIVE!!):-\t")
rev=x[::-1]
if rev==x:
    print(x,"Is A Palindrome!!")
else:
    print(x,"Is Not A Palindrome!!")