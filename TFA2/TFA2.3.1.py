fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

sliced = fname[0:3]

print("Full Name:", fname + " " + lname)
print("Sliced Name:", sliced)
print("Greeting Message: Hello " + sliced + "! Welcome. You are " + age + " years old.")