#!/usr/bin/env python3
file = open("spider.txt")

# readline() read the line from the current position
print(file.readline())

# read the second line of the file (before the current position is the second,
# after is the third)
print(file.readline())

# This command read the current position to the end of the file
print(file.read())

file.close()


# the command with you dont need to insert the close() command, and you work
# with this file only in the 'with' enviroment
with open("spider.txt") as file:
  print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
print(lines)

