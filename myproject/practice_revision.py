# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum = num1 + num2

# diff = num1 - num2

# product = num1 * num2

# div = num1 / num2

# print(f"sum {sum} , diff {diff} , product {product} , div {div}")


# print("Enter the number :")

# num = int(input())

# if num < 0:
#     print("negative number")
# elif num > 0:
#     print("positive number")
# else:
#     print("zero")


# age = int(input("Enter the age :"))

# if age > 13 and age < 19:
#     print("teenager")
# elif age <= 20 and age < 59:
#     print("adult")
# else :
#     print("senior citizen")


import random 

super_number = random.randint(1,10)
attempts = 0

print("Guess number between 1 to 10")

while True:
    guess = int(input("Enter your guess: "))