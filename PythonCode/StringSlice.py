text = "Python Programming"

# Slicing strings
print(text[0:6])   # Output: Python
print(text[7:18])  # Output: Programming
print(text[:6])    # Output: Python
print(text[7:])    # Output: Programming
print(text[-11:-1]) # Output: Programming (excluding the last character)


text = "Python Programming"

# Slicing with step
print(text[::2])   # Output: Pto rgamn (every 2nd character)
print(text[1::3])  # Output: yh rga (starting from index 1, every 3rd character)
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses the string)

text = "Python Programming"

# Find index of substring
index_of_programming = text.find("Programming")
print(index_of_programming)  # Output: 7 (starting index of "Programming")

# Find index of character
index_of_p = text.index("P")
print(index_of_p)  # Output: 0 (first occurrence of 'P')
