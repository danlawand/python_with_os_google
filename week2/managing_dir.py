#!/usr/bin/env python3
import os
if os.path.isdir("new_dir") == False:
    os.mkdir("new_dir")

os.chdir("new_dir")
print(os.getcwd())

os.mkdir("newer_dir")

# remove only empty directories
os.rmdir("newer_dir")


os.mkdir("other_dir")

# Just creating files
with open("he-man.txt", "w") as file:
    file.write("Eu tenho a forçaaa")
with open("iron-man.txt", "w") as file:
    file.write("I am Iron Man")

dir = "./"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
        os.rmdir(name)
    else:
        print("{} is a file".format(fullname))
        os.remove(fullname)
os.chdir("./..")
os.rmdir("new_dir")
print("new_dir and its contents were removed")



