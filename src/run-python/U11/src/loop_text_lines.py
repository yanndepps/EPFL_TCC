# read each line of the file until there are no more
text_file = open("../assets/myfile.txt")
for line in text_file:
    print(line)

# always close data file
text_file.close()
