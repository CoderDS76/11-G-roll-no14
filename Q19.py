def menu():
    print()
    print("TEXT STUFF")
    print()
    print("[1] Count number of words")
    print("[2] Count number of characters")
    print("[3] Count number of vowels")
    print("[4] Count number of digits")
    print("[5] Count number of alphabets")
    print("[0] Exit")
    print()

#Defining Menu
menu()
n=int(input("Enter your choice:   "))
print()
while n!=0:
    if n==1:
        sen=input("Enter the string:   ")
        print()
        print("The number of words in the string is:  ",len(sen.split()))
    elif n==2:
        sen=input("Enter the string:   ")
        print()
        countch=0
        for ch in sen:
            if ch!=" ":
                countch+=1
        print("The number of Characters in string is:  ",countch)    
    elif n==3:
        sen=input("Enter the string:   ")
        print()
        vowels=["a","e","i","o","u"]
        countvowel=0
        for ch in sen:
            if ch.lower() in vowels:
                countvowel+=1
        print("The number of Vowels in the string is:  ",countvowel)
    elif n==4:
        sen=input("Enter the string:   ")
        print()
        countdig=0
        for ch in sen:
            if ch.isdigit():
                countdig+=1
        print("The number of Digits in the string is:   ",countdig)
    elif n==5:
        sen=input("Enter the string:   ")
        print()
        countalpha=0
        for ch in sen:
            if ch.isalpha():
                countalpha+=1
        print("The number of Alphabets in the string is:   ",countalpha)
    else:
        print("INVALID CHOICE!!")
    menu()
    n=int(input("Enter your choice:   "))
    print()
    #All Conditions
print("Thank You For Using TEXT STUFF")
#End of code