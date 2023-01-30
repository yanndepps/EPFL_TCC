# Ex: Guess the number and the color
import random


def play():
    in_1 = input("guess a color: ")
    in_2 = input("guess a number between 1 and 20: ")

    color = "blue"
    # num = 9
    num = random.randrange(1, 21)

    mess_1 = "you've found both the secret number and the secret color !"
    mess_2 = "you've found at least one secret !"
    mess_3 = "you didn't find any of the secrets !" + "\n" + "Better luck next time !"

    if int(in_2) == num and in_1 == color:
        print(mess_1)
    elif int(in_2) == num or in_1 == color:
        print(mess_2)
    else:
        print(mess_3)

    print("Try again !")
    print("The number was: " + str(num))
    print("The color was: " + color)


play()
