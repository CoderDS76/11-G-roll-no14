string=input("Enter any string:-\t")
list=['a','e','i','o','u','A','E','I','O','U']
n=0
for i in string:
    if i in list:
        n+=1
print(n)