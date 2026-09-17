def rotate_right(lst):
    # Handle empty lists gracefully
    if not lst:
        return lst
    
    # Take the last element and append the rest of the list (excluding the last element)
    return [lst[-1]] + lst[:-1]

# Example usage:
my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_right(my_list)

print("Original List:", my_list)
print("Rotated List: ", rotated_list)
