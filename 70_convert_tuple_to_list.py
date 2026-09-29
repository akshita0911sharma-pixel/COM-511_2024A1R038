3. WAP to show that tuple values cannot be changed directly. Convert tuple into list , update it and convert it back into tuple.

tup=("Jammu",1,2,4,5,"Akhnoor")
t=list(tup)
print(t)
t.append("HappyHoliday")
print(tuple(t))
