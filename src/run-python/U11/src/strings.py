# Python text magic
# Strings
# --
# text = "Hello, You!"
# print(text[1])
# print(len(text))

# everything between position a and b
# ---
# print(text[7:10])

# remove start and end trailing spaces
# ---
# text = "   Hello, Space!   "
# stripped = text.strip()
# print(stripped)

# ensure whitespaces are removed in an input message
# ---
# message = input("Enter a message for Yann: ")
# print(message.strip() + " Yann!")

# the function can be chained
# ---
# message = input("Enter a message for Yann: ").strip()
# print(message + " Yann!")

# to upper or lower case
# ---
# word = "KiWi"
# print(word.upper())
# print(word.lower())

# replace parts of a string
# the function replace() returns a new string and therefore
# does not modify the original one ! -> store the result in a new var
# ---
# text = "Hello Yann"
# replaced = text.replace("Yann", "Golden Snake")
# print(replaced)

# the split() function turns a string into an array of words
# ---
# words = "Apples,Bananas,Oranges"
# array = words.split(",")
# for word in array:
#     print(word)

# escape sequence -> \n, \t, etc ...
# ---
# message = "Hello\nYou!"
# message = "Hello \n You!"
# rep = message.replace(" ", "")
# print(rep)

# find something inside a string
# ---
# message = "Hello You, what is the weather like outside?"
# is the word "weather" part of this string ?
# will return the index position at which the word starts -> ( 23 )
# will return -1 if not found
# result = message.find("weather")
# result = message.find("oranges")
# print(result)

# all those functions can be chained
# ---
# text = "   Hello You   "
# message = text.strip().upper().replace("YOU", "YANN")
# print(message)
