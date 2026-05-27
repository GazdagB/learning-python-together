import random

#Initial State of the program
isSolved = False

# Generate random computer number to guess
compsRandomNumb = random.randint(1, 100)

while not isSolved:

    x = input("Enter a number (0 - 100): ")
    digit = 0
    if not  x.isdigit():
        print("The input must be a number!")
        continue

    digit = int(x)

    if digit <= 0 or digit > 100:
        print("Number must be between 0 and 100!")
        continue

    if digit == compsRandomNumb:
        print("The number is correct! It was {}!".format(compsRandomNumb))
        isSolved = True
    elif digit > compsRandomNumb:
        print("Too high! Guess Downward!")
    elif digit < compsRandomNumb:
        print("Too low! Guess Upper!")