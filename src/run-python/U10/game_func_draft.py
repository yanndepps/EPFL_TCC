# Guess a Number Game
# ---
import random

ran_num = random.randint(1, 100)
show_debug = True
debug = "The secret number is : " + str(ran_num)
if show_debug:
    print(debug)


def guess_game():
    # --- vars
    play_game = True
    attempts = 0
    guess = input("Pick a number between 1 and 100 : ")
    congrats = "Got it ! You made it in "
    not_a_num = "This is not a valid number !"
    num_major = "Try a bigger number : "
    num_minor = "Try a smaller number : "

    # --- logic
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

guess_game()
