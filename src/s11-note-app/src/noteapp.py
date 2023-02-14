# Terminal Notes Taking
# ---
# DONE: need to move on ...
# WARN: case sensitive -> "World" != "world"
# WARN: does not allow substrings -> "dog" will not be found within "dogs"
# TODO: how to display a message if !word ?
# TODO: bring back punctuations when displaying result ?
# ---


def main():
    # --- where do we store our notes?
    path = "../assets/notes.txt"

    # --- choose an option at start
    ask = "What do you want to do?"
    choice_1 = "Press 1 for adding a note"
    choice_2 = "Press 2 for searching your notes"
    enter_note = "Enter your note:" + "\n"
    search_note = "Enter the text to search:" + "\n"
    dashes = "---"
    welcome = ask + "\n" + choice_1 + "\n" + choice_2 + "\n" + ": "
    prompt = input(welcome)

    # --- conditions : 1 or 2
    if prompt == "1":
        with open(path, mode="a", encoding="utf-8") as f:
            new_note = input(enter_note)
            f.write(new_note + "\n")
    elif prompt == "2":
        with open(path, mode="r", encoding="utf-8") as f:
            # load data, remove empty line and punctuations
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            lines = [
                line.replace("!", "")
                .replace(",", "")
                .replace(".", "")
                .replace("?", "")
                .replace("-", " ")
                .replace(":", "")
                for line in lines
            ]
            # print(lines)

            # confirm we do not load empty lines
            # print("num of lines is {}".format(len(lines)))

            # loop through the list and display our word if found
            word = input(search_note)
            for i, line in enumerate(lines):
                if word in line.split():  # line.split() for full words search
                    print('The word "{}" is found in line {} : '.format(word, i + 1))
                    print(line)
                    print(dashes)

    # if none of our choices are met
    else:
        print("Nope!")
        quit()


# --- run main function
main()
# --- END
