# Reverse a string using a for loop

text = input("Enter a string: ")

reverse = ""

for character in text:
    reverse = character + reverse

print("Original string:", text)
print("Reversed string:", reverse)