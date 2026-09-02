# Count vowels in a string

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():

    if character in vowels:
        count = count + 1

print("Number of vowels:", count)