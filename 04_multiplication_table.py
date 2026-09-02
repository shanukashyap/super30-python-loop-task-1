# Print multiplication table from 1 to 20

number = int(input("Enter a number: "))

for i in range(1, 21):
    print(number, "x", i, "=", number * i)