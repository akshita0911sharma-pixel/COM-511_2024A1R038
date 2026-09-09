 #WAP to input four numbers from the user and find the greatest number among them. 

numbers = []

for i in range(4):
    num = int(input("Enter a number: "))
    numbers.append(num)

greatest = max(numbers)
print("Greatest number is:", greatest)
