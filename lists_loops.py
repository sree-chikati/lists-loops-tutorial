#Task: Copy the above list songs into your list_loops.py file
songs = ["ROCKSTAR", "Do It", "For The Night"]

#Task: print out the first and last element of the songs list in your list_loops.py file
print(songs[0])
print(songs[2])

#Task: print out "Do It"and "For The Night" using a list slice on the songs list in your list_loops.py file
print(songs[1:3])

#Task: update the last element in the songs list with a new song of your choice in your list_loops.py file
songs[2] = "Butterfly"
print(songs)

#Task: add three songs of your choice to your songs list in your list_loops.py file
songs.append("Run") #adds an element to the end of the list
print(songs)
songs.extend(["Save Me"]) #adds a list to end of a list
print(songs)
songs.insert(4, "Spring Day") #adds element at specific index followed by item
print(songs)