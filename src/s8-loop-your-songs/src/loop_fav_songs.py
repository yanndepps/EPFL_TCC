# Ex : Loop through your favorite songs
# ---

fav_songs = [
    "Exquisite Human Microphone",
    "Crimson Ways",
    "Bleeding Ink",
    "Old Thought",
]

fav_order = ["First: ", "Second: ", "Third: ", "Fourth: "]

message = "These are my favorite songs: "
ask = "What are yours ?"

print(message)

init_val = 0
max_val = len(fav_songs)
while init_val < max_val:
    print(fav_order[init_val] + " " + fav_songs[init_val])
    init_val = init_val + 1


print(ask)

# ---
