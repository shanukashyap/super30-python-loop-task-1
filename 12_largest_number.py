# Find the largest number without using max()

numbers = [12, 45, 23, 89, 34, 67]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest number:", largest)