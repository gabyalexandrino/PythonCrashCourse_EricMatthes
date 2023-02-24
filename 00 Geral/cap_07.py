# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# promt = "If you tell us who you are, we can personalize the messages you see."
# promt += "\nWhat is your first name? "
# name = input(promt)
# print("\nHello, " + name + "!")

# age = input("How old are you? ")
# age = int(age)
# print(age + " >= 18?")
# print(age >= 18)

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

print(4 % 3)
print(5 % 3)
print(6 % 3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")