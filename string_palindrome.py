string1=input("Enter any string:-\t")
length=len(string1)
string2=""
for i in range(1,length+1):
    string2=string2+string1[-i]
if string2==string1:
    print(string2,"Palindrome!!")
else:
    print(string2,"Not a palindrome!!")