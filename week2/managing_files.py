#!/usr/bin/env python3

import os
import datetime

if os.path.exists("guests.txt"):
    os.remove("guests.txt")
    print("guests.txt removed")
else:
    print("guests.txt doesnt exist")

if os.path.exists("first_draft.txt"):
    os.rename("first_draft.txt", "finished_masterpiece.txt")
    print("first_draft.txt renamed to finished_masterpiece.txt")
else:
    print("first_draft.txt doesnt exist")

if os.path.isfile("spider.txt"):
    print("Absolute path: ", os.path.abspath("spider.txt"))
    print("Size of the file: ", os.path.getsize("spider.txt"))
    creation_time = os.path.getmtime("spider.txt")
    print("Creation time: ", datetime.datetime.fromtimestamp(creation_time))

else:
    print("spider.txt is not a file")

