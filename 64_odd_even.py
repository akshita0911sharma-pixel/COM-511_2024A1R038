# Program to separate even and odd numbers from a list

# 1. Take space-separated numbers as input from the user
user_input = input("Enter numbers separated by spaces: ")

# 2. Convert the input string into a list of integers
numbers = [int(num) for num in user_input.split()]

# 3. Create separate lists for even and odd numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# 4. Display the results
print("\n--- Results ---")
print("Original List:    ", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List: ", odd_numbers)
