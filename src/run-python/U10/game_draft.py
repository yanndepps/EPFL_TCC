# Guess the Number ( draft )
# Write a game with the following rules :
# ---
# 1. when starting the game, a secret number between 1 and 100 is generated
# 2. the game asks the user to enter a number
# 3. the game will tell the user if the secret number is bigger or smaller than the guess
# 4. as long as the user doesn't find the secret number, the game continues
# 5. as soon as the user finds the secret number, the game stops and tells the user
#    how many attempts it took to win
# 6. in case the user enters anything else than a number, the game should tell and quit
# ---
import random

ran_num = random.randint(1, 100)
debug = "The secret number is : " + str(ran_num)
print(debug)

attempts = 0
play_game = True

guess = input("Pick a number between 1 and 100 : ")
congrats = "Got it ! You made it in "
not_a_num = "This is not a valid number !"
num_major = "Try a bigger number : "
num_minor = "Try a smaller number : "


while play_game:
    # try & catch for sring inputs instead of integers
    try:
        res = int(guess)
    except:
        print(not_a_num)
        quit()

    # bigger, smaller or correct guess. count the attempts
    if guess > str(ran_num):
        attempts += 1
        guess = input(num_minor)
    elif guess < str(ran_num):
        attempts += 1
        guess = input(num_major)
    elif guess == str(ran_num):
        attempts += 1
        print(congrats + str(attempts) + " attempts !")
        play_game = False

# ---
