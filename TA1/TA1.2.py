#A program that will count the sum of the digits from a given input string digits.

sum = 0
text = input("Enter a string: ")

for char in text:
    if char.isdigit():
        sum += int(char)

print("Sum of digits:", sum)

