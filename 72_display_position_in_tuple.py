5. WAP to check whether a given value is present in a tuple. If present, display its position.

numbers=(10,20,30,40,50)

search=int(input("Enter number to search:"))
found=False
for i in range(len(numbers)):
    if numbers[i]==search:
        print("element found at position:",i)
        found=True
        break
if found==False:
    print("Element not found.")
