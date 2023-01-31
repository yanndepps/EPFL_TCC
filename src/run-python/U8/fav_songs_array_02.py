# Manipulating your own array
# ---
# 1. Sort by alphabetical order
# 2. Display each song on its own line in the terminal
# 3. Add a 5th song at the end of the array
# 4. Display how many songs are in the array within a sentence ("there are x songs ...")
# 5. Remove the 3rd song in the array
# 6. Display the content of the array on one line
# 7. Display the length of the array
# ---

fav_songs = [
    "Exquisite Human Microphone",
    "Crimson Ways",
    "Bleeding Ink",
    "Old Thought",
]


# --- 1 --- #
fav_songs.sort()
print(fav_songs)
print("# ---")

# --- 2 --- #
print(fav_songs[0])
print(fav_songs[1])
print(fav_songs[2])
print(fav_songs[3])
print("# ---")


# --- 3 --- #
fav_songs.append("Decay Waves")


# --- 4 --- #
# fav_songs.pop(1)
# fav_songs.pop(1)
# fav_songs.pop(1)
# fav_songs.pop(1)

num_songs = len(fav_songs)
mess_1 = "There are " + str(num_songs) + " songs in the array !"
mess_2 = "There is only " + str(num_songs) + " song in the array !"
if num_songs == 1:
    print(mess_2)
else:
    print(mess_1)


# --- 5 --- #
fav_songs.pop(2)
print("# ---")

# --- 6 --- #
print(fav_songs)
print("# ---")

# --- 7 --- #
print(len(fav_songs))
print("# ---")

# ---
