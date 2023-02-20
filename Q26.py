d={}
#Making Empty Dictionary
num=int(input("Enter number of entries:  "))
#Taking number of entries
keys=[]
values=[]
#Making list for input
for i in range(1,num+1):
    key=i
    value=int(input("Enter the Value:  "))
    keys.append(key)
    values.append(value)
    #Taking Data from user
for i in range(0,num):
    d[keys[i]]=values[i]
    #Adding all data to Dictionary
print("The maximum and minimum value in the dictionary is:  ",max(d.values()),min(d.values()),"respectively")
#Printing
#End of Code