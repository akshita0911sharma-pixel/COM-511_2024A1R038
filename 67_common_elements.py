# Input two lists from the user (elements separated by spaces)
list1 = input("Enter elements for the first list (space-separated): ").split()
list2 = input("Enter elements for the second list (space-separated): ").split()

# Find common elements using set intersection and convert back to a list
# (This also automatically handles duplicate entries)
common_list = list(set(list1) & set(list2))

# Display the results
print("First List:", list1)
print("Second List:", list2)
print("3rd List (Common Elements):", common_list)
