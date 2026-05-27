import random
import time

RED = "\033[91m"
RESET = "\033[0m"

def create_random_array(length):
    array = []

    for i in range(length):
        array.append(random.randint(0, 100))

    return array


def print_array(array, tracked_number):

    colored_array = []

    for num in array:

        if num == tracked_number:
            colored_array.append(f"{RED}{num}{RESET}")
        else:
            colored_array.append(str(num))

    print("[" + ", ".join(colored_array) + "]")


def process_array(array):

    # Pick one number to track
    tracked_number = array[0]

    print(f"Tracking number: {RED}{tracked_number}{RESET}")
    print("-" * 30)

    while len(array) > 0:

        # Add new number to beginning
        new_number = random.randint(0, 100)
        array.insert(0, new_number)

        # Remove 2 items from the end safely
        if len(array) > 0:
            array.pop()

        if len(array) > 0:
            array.pop()

        print_array(array, tracked_number)

        print("-" * 30)

        # Stop if tracked number disappeared
        if tracked_number not in array:
            print(f"{RED}{tracked_number}{RESET} was removed!")
            break

        time.sleep(0.3)
    print("Array is empty!")


my_array = create_random_array(100)

process_array(my_array)