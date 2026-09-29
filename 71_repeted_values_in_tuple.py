4. WAP to store repeated values in a tuple and count how many times a given value appears.

l=[]
tup=(1,2,3,4,3,1,2,34,3,5,66)
for i in tup:
    count=0
    for j in tup:
        if i==j:
            count+=1
    
    if i not in l:
        print(f"{i} appears {count} times")
        l.append(i)
