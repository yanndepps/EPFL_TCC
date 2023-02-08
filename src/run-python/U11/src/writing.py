# Writing to a file
# ---
# create a file and write
# file = open("../assets/write_a_file.txt", "w")
# file.write("Hey!")
# file.close()

# open and append to an existing file
file = open("../assets/write_a_file.txt", "a")
file.write("\nWhat's up ?")
file.close()
