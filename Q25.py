import json
d={}
#Making empty dictionary
num=int(input("Enter number of entries:  "))
#Taking number of entries
rno=[]
name=[]
marks=[]
#Making lists for roll, name and marks for input
for i in range(1,num+1):
    roll=int(input("Enter the Roll no:  "))
    nme=input("Enter the Name:  ")
    mrks=int(input("Enter the Marks:  "))
    rno.append(roll)
    name.append(nme)
    marks.append(mrks)
    #Entering all data from user
for i in range(0,num):
    d[rno[i]]=[name[i],marks[i]]
    #Adding data in dictionary
print(json.dumps(d))
#Printing
#End of Code