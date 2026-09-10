import random

# Ask the player to choose a level
print("Choose a level!")
print("Easy = 10 tries")
print("Hard = 5 tries")

level = input("Input chosen level: ")

if level == "Easy":
    attempts = 10
else:
    attempts = 5

# Create a random secret number between 1 and 100
secret_number = random.randint(1, 100)

print("\nI am thinking of a number between 1 and 100.")
print("You have", attempts, "tries. Good luck!\n")

guess_count = 0
won = False

while guess_count < attempts:
    guess = input("Enter your guess: ")
    guess = int(guess)
    guess_count = guess_count + 1

    if guess < secret_number:
        print("Too Low!\n")
    elif guess > secret_number:
        print("Too High!\n")
    else:
        print("Correct! You guessed it in", guess_count, "tries!")
        won = True
        break

if not won:
    print("\nOut of tries! The number was", secret_number)
