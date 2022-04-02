#!/usr/bin/env python3
# open("new_file.txt", "w")
# "r" read-only
# "w" write only
# "a" append
# "r+" read-write
# more info in https://docs.python.org/3/library/functions.html#open
with open("new_file.txt", "w") as file:
    file.write("Hello world, I am a programmer")
    # returns the number of char that we are wiriting

