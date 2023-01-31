# Loops in Python
# 1. -> For loops

# for x in range(4):
#     print(x)


# Ex:
# for x in range(4):
#     print("Number: " + str(x))

# Ex:
for i in range(5):
    current_step = str(i + 1)
    step_word = ""
    if current_step == "1":
        step_word = " step"
    else:
        step_word = " steps"
    print("It's " + current_step + step_word)
