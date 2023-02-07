# The guest list
contacts_list = open("../assets/contacts.txt")

# read & print line by line
for line in contacts_list:
    print(line)

# always close the data file
contacts_list.close()
