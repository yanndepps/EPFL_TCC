# Note Taking App -> Walkthrough
# ---

# create a note
def write_note(text):
    file = open("../assets/walkthrough.txt", "a")
    file.write("---\n")
    file.write(text + "\n")
    file.close()


# search through notes
def search(text):
    # the param "r" is optional and implicit
    file = open("../assets/notes.txt")
    content = file.read()
    file.close()
    result = ""
    notes = content.split("---")
    for note in notes:
        if note.find(text) != -1:
            result += "\n---" + note
    if result == "":
        print("nothing found!")
    else:
        print(result)


# display menu
print("what do you want to do?")
print("press 1 for adding a note")
print("press 2 for searching your notes")
answer = input(": ")

# execute task based on menu input
if answer == "1":
    print("enter your note:")
    note = input().strip()
    write_note(note)
elif answer == "2":
    print("enter the text to search")
    text = input().strip()
    search(text)
else:
    print("sorry! I didn't understand that!")
