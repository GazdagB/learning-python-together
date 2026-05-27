import random

#Initial State of the program
isSolved = False

# Generate random computer number to guess
compsRandomNumb = random.randint(1, 100)

while not isSolved:

    x = input('\x1b[0m' + "Enter a number (0 - 100): ")
    digit = 0
    if not  x.isdigit():
        print("\033[31m The input must be a number! \033[31m"  )
        continue

    digit = int(x)

    if digit <= 0 or digit > 100:
        print("\033[31mNumber must be between 0 and 100!\033[31m")
        continue

    if digit == compsRandomNumb:
        print("\033[32mThe number is correct! It was {}! \033[32m".format(compsRandomNumb))
        isSolved = True
    elif digit > compsRandomNumb:
        print("⬇️ Too high! Guess Downward!")
    elif digit < compsRandomNumb:
        print("⬆️ Too low! Guess Upper!")