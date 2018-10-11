# This code will create a file called "bigfile.txt" and generate data a "a to z" (see ascii) on 100 lines.

from string import ascii_uppercase

with open("bigfile.txt", "a") as f: # a stands for append. If you want to write over a file use "w."
    for i in range(100):
        f.write(ascii_uppercase + "\n")