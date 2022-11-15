number=int(input("Enter the number to be checked:-\t"))
sum=0
times=0
temp=number
while temp>0:
    times+=1
    temp=temp//10
temp=number
while temp>0:
    remainder=temp%10
    sum=sum+(remainder**times)
    temp//=10
if number==sum:
    print(number,"Is Armstrong!!")
else:
    print(number,"Is Not Armstrong!!")