n=int(input("Enter the number of terms (Greater than 1): "))
#Taking number of terms
if n>1:
    tup1=tuple((input("Enter the first term: ")))
    for i in range(1,n):
        tup2=tuple((input("Enter the next term: ")))
        tup1+=tup2
        #Making the tuple
    x={}
    for i in tup1:
        if tup1.count(i)>1:
            x[i]=tup1.count(i)
            #Entering in dictionary
    for keys in x:
        print(keys)
        #printing keys of dictionary, will give all repeated items
#End of code