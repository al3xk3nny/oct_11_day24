# Open the file data.txt and save a handle to the file in f.
with open("data.txt") as f:
    # Read the entire contents of the file into text.
    text = f.read()


# Print the contents of text to the console.
print(text)