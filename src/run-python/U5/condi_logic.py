# conditional logic
# password = "secret"
# user_input = input("enter password: ")

# if password == user_input:
#     print("logged !")

# ---
# apples = 7
# oranges = 9

# if apples > oranges:
#     print("more apples in the bag!")
# else:
#     print("more oranges in the bag!")

# ---
# display a calculation and check for result
# def calc(a, b):
#     inp = input("What is the result of " + str(a) + " + " + str(b) + " ? ")
#     add = a + b
#     success = "The program terminated successfully ! "
#     congrat = "Congrats the result is correct! "
#     shame = "Not too late to learn! "
#     result = "The result of " + str(a) + " + " + str(b) + " is " + str(add)
#     if add == int(inp):
#         return congrat + "\n" + result + "\n" + success
#     else:
#         return shame + "\n" + result + "\n" + success


# print(calc(5, 2))

# secret word updated
password = "kiwi"
guess = input("what is the secret word ? ")
if password == guess:
    print("congrats !")
else:
    print("play again ?")
