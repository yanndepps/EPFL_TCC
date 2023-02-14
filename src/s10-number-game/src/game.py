# Guess a Number Game
# ---
import random

ran_num = random.randint(1, 100)

# show or hide the secret number at the start
show_debug = True
debug = "The secret number is : " + str(ran_num)
if show_debug:
    print(debug)


def guess_game():
    # --- vars
    play_game = True
    attempts = 0
    guess = input("Pick a number between 1 and 100 : ")
    congrats = "Nailed it ! In"
    not_a_num = "This is not a valid number !"
    num_major = "Try a bigger number : "
    num_minor = "Try a smaller number : "
    count_singular = "attempt !"
    count_plural = "attempts !"

    # --- logic
    while play_game:
        # try & catch for numbers only
        try:
            res = int(guess)
        except:
            print(not_a_num)
            quit()

        # increment game turns
        attempts += 1

        # one attempt -> singular
        if attempts == 1:
            count_word = count_singular
        else:
            count_word = count_plural

        # bigger, smaller or correct guess
        if res > ran_num:
            guess = input(num_minor)
        elif res < ran_num:
            guess = input(num_major)
        elif res == ran_num:
            print(congrats + " " + str(attempts) + " " + count_word)
            play_game = False


# ---

guess_game()
