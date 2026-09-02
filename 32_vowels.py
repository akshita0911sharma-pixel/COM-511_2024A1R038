text=input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print(vowel_count)  
