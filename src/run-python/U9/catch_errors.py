# Catching Errors
# ---

num = input("type a number ")

try:
    res = int(num) + 1
except:
    print("could not convert your input to a valid integer number!")
    quit()

print("the result is " + str(res))
