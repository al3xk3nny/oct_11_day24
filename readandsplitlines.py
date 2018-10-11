f = open("data.txt")

text = f.read().split("\n") # In this example, we do the split ourselves and strip out the "\n" characters.

f.close()

print(text) # Prints out lines as a list.

for l in text: # Prints out lines on seprate list as per "data.txt" file.
    print(l)