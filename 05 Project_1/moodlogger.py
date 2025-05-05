from datetime import datetime
# Daily Mood Logger 

# Ask the user how they are feeling today
mood = input("Hey, how are you feeling today?")

print("You are feeling " + mood)

# Add timestape to the mood
with open("mood.txt", "a") as file:
    # Write the mood to the file
    file.write(f"{datetime.now()}: {mood}\n")