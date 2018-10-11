# Open the file data.txt and save a handle to the file in f (f is a variable that gives us acess to the file we have opened).
f = open("data.txt")

# Read the ENTIRE contents of the file into text.
text = f.read()

# Close the file
f.close()

# Richard advises to always work with data in memory. In other words, open the file, read the entire contents and close it, then work with contents.

# Print the contents of text to console.
print(text)
