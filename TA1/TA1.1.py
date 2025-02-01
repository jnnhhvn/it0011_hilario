#A program that will display the number of vowels, consonants, spaces, and other characters given an input string.

vowels = 0 
consonants = 0 
spaces = 0 
others = 0
vowel_chars = "AEIOUaeiou"

text = input("Enter a string: ")

for char in text:
    if char.isalpha():
        if char in vowel_chars:
            vowels += 1
        else:
            consonants += 1
    elif char.isspace(): 
        spaces += 1
    else:
        others += 1

print("--------------------------------")
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Spaces: ", spaces)
print("Other characters: ", others)
