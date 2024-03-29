#!/usr/bin/env python3

# Populating
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# Verifying expected: Bob, Andrea, Manuel, Polly, Khalid
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#new_guests checkin
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# Verifying expected: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.
with open("guests.txt") as guests:
    for line in guests:
        print(line)

# checkout
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# Verifying expected: Bob, Polly, Sam, Danielle and Jacob.
with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Verifying if X and Y still in the hotel
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

