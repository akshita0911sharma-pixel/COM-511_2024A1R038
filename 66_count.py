#write a python program to count how many times a particular element appears
# Step 1: Get a list of elements from the user
user_list_input = input("Enter list elements separated by spaces: ")

# Convert the input string into a list of items
elements = user_list_input.split()

# Step 2: Get the specific element to count
target = input("Enter the element you want to count: ")

# Step 3: Count the occurrences using the count() method
frequency = elements.count(target)

# Step 4: Display the result
print(f"\nThe element '{target}' appears {frequency} time(s) in the list: {elements}")
