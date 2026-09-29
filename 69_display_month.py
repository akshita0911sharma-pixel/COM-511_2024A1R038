2. WAP to store all month names in a tuple. Input a month number and display the corresponding month name.

n=int(input("Enter number:"))
tup=((1,"January"),(2,"Feb"),(3,"March"),(4,"April"),(5,"May"),(5,"June"),(7,"July"),(8,"August"),(9,"September"),(10,"October"),(11,"November"),(12,"December"))

for i in tup:
    if i[0]==n:
        print(i[1])
