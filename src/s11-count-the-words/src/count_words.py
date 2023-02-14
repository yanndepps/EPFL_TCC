# Ex: Count the Words
# ---
# --- load and read our data
zen = open("../assets/zen_of_python.txt")
content = zen.read()

# --- remove special chars
# create a list of chars replacement using tuples
chars_to_rmv = [
    ("it's", "it is"),
    ("let's", "let us"),
    ("n't", " not"),
    ("'re", " are"),
    (",", ""),
    (".", ""),
    ("*", ""),
    ("!", ""),
    ("-", ""),
    ("\n", " "),
    ("  ", " "),
]
# store the original data into a new var to handle further manipulation
rmv_chars = content

# iterate over the tuples and replace by populating
# the arguments with the old and new vars
for old, new in chars_to_rmv:
    rmv_chars = rmv_chars.replace(old, new)

# --- display the number of words -> 140
count_words = rmv_chars.split(" ")
message = "The Zen of Python contains " + str(len(count_words)) + " words."
print(message + "\n" + "# ---")
# print(rmv_chars)
# print(count_words)

# --- replace every instance of "is" by "should be"
# --- convert the text to uppercase
# --- bring back both punctuation and special chars
content = content.replace("is", "should be").upper()
print(content)

# --- close the data file
zen.close()
