unit=int(input("Enter the number of units used:-\t"))
price=50
if unit>100:
    unit2=unit-100
    if unit2>200:
        unit3=unit-300
        price+=(0.4*100)+(0.5*200)+(0.6*unit3)
    else:
        price+=(0.4*100)+(0.5*unit2)
else:
    price+=(0.4*unit)
print("Your electric bill is",price,"(METER CHARGE INCLUDED!)")