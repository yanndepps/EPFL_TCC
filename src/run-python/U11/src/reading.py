# opening a file
text_file = open("./myfile.txt")

# reading the content
content = text_file.read()

print(content)

# closing the file ( needed! )
text_file.close()
