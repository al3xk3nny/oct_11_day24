f = open("data.txt")

text = f.readlines() # Richard doesn't like this as it leaves in the /n characters for some reason. He recommends using read and split lines instead.

f.close()

print(text)
