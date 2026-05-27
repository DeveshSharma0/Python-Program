a = "DEVESH"
#accessing the string using string indexing
short = a[0:7]
print(short)

# Negative Indexing
short = a[-6:7]
print(short)

print(a.capitalize()) # Capitalize the first letter of the string
print(a.lower()) # Convert the string to lowercase\
print(a.upper()) # Convert the string to uppercase
print(a.title()) # Convert the first letter of each word to uppercase
print(a.swapcase()) # Swap the case of each letter in the string
print(a.count("E")) # Count the number of occurrences of a substring in the string
print(a.find("E")) # Find the index of the first occurrence of a substring in the string
print(a.replace("E", "X")) # Replace all occurrences of a substring in the string
print(a.strip("D")) # Remove the specified characters from the beginning and end of the string
print(a.split("E")) # Split the string into a list using the specified separator
print(a.join("123")) # Join the elements of a list into a string using the specified separator
print(a.startswith("D")) # Check if the string starts with the specified substring
print(a.endswith("H")) # Check if the string ends with the specified substring
print(a.isalpha()) # Check if all characters in the string are alphabetic
print(a.isdigit()) # Check if all characters in the string are digits
print(a.isalnum()) # Check if all characters in the string are alphanumeric
print(a.islower()) # Check if all characters in the string are lowercase
print(a.isupper()) # Check if all characters in the string are uppercase
print(a.isspace()) # Check if all characters in the string are whitespace
print(a.startswith("D")) # Check if the string starts with the specified substring
print(a.endswith("H")) # Check if the string ends with the specified substringprint(a.isupper()) # Check if all characters in the string are uppercase
print(a.isspace()) # Check if all characters in the string are whitespace




#lower string in List to Convert in Upper
a = ["a", "b", "c", "d", "e", "f"]
final = [x.upper() for x in a]
print(final)

# using split() method to split the string into a list
a = "Devesh, Kumar, Sharma, 123, 456, 789, 012"
d = a.split(", ")
print(d)
