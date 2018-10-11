import re # Imports regular expressions to be used in document below.
import collections # Imports collections to be used in the document below.

# Challenge 1
# Open the file "1155-0.txt" and readt the ENTIRE contents. Then print out number of characters.
# with open("1155-0.txt") as f:
#     text = f.read()
    
# print(len(text))   


# Challenge 2
# Count the words in the file.
# with open("1155-0.txt") as f:
#     text = f.read()

#     words = text.split(" ")
    
# print(len(words))


# How many words?.
# with open("1155-0.txt") as f:
#     text = f.read()

#     words = text.split(" ")
    
# print(len(words))


# Using a regular expression to find words only
# with open("1155-0.txt") as f:
#     text = f.read()

#     words = re.findall("\w+", text) # "\w+"" is the regular expression for any word character equal to [a-zA-Z0-9_].
    
# print(len(words))


# Finding unique words in the file using the set() data structure.
# with open("1155-0.txt") as f:
#     text = f.read()

#     words = re.findall("\w+", text)

# unique_words = set(words)

# print(len(words))
# print(len(unique_words))


# Finding the top ten most commonly used words using collections (counter(words).most_common) 
# with open("1155-0.txt") as f:
#     text = f.read()

#     words = re.findall("\w+", text)

# top_10 = collections.Counter(words).most_common(10)

# print(top_10)


# Finding the top five most commonly used words with length of more than or equal to five characters.
with open("1155-0.txt") as f:
    text = f.read()

    words = re.findall("\w+", text)
    
# Filter "words" and keep only those with 5 letters or more.
long_words = []
for word in words:
    if len(word) >= 5:
        long_words.append(word)
        
# List comprehension of the above is; long_words = [word for word in words if len(word) >= 5]. The "word" to the left of the for statement is the item that is entered into the list, so you don't need the append.

top_5 = collections.Counter(long_words).most_common(5)

print(top_5)