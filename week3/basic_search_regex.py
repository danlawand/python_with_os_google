#!/usr/bin/env python3

import re

# 'r' =  rawstring => python interpretor não deve tentar interpretar qualquer
# carcter especial. Ou seja, vai ser entendido como um comando em regex

result = re.search(r"aza", "plaza")
print("'aza' em 'plaza': {}".format(result))
# 'aza' em 'plaza': <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print("'aza' em 'bazaar': {}".format(result))
# 'aza' em 'bazaar': <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "banze")
print("'aza' em 'banze': {}".format(result))
# 'aza' em 'banze': None

print("'^x' em 'xenon': {}".format(re.search(r"^x", "xenon")))
# '^x' em 'xenon': <re.Match object; span=(0, 1), match='x'>

print("'^x.' em 'xenon': {}".format(re.search(r"^x.", "xenon")))
# '^x.' em 'xenon': <re.Match object; span=(0, 2), match='xe'>

print("'p.ng' em 'penguin': {}".format(re.search(r"p.ng", "penguin")))
# 'p.ng' em 'penguin': <re.Match object; span=(0, 4), match='peng'>

print("'p.ng' em 'Pangaea': {}".format(re.search(r"p.ng", "Pangaea", re.IGNORECASE)))
# 'p.ng' em 'Pangaea': <re.Match object; span=(0, 4), match='Pang'>

print(re.search(r"[Pp]ython", "python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "What a way to go"))

print(re.search(r".+[a-z]way", "The end of the highway"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[,.\"\'?!]", "Ola,  Tudo bem com vc? "))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))

print(re.search(r"cat|dog", "I like dogs."))

print(re.search(r"cat|dog", "I like cats and dogs."))

print(re.findall(r"cat|dog", "I like cats and dogs."))

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l", "goldfish"))

print(re.search(r"o+l", "woolly"))

print(re.search(r"o+l", "boil"))


#################################################

def repeating_letter_a(text):
  result = re.search(r"[a|A].*[a|A]", text)
  return result != None

print("{} that 'banana' there is more than 1 'a|A'".format(repeating_letter_a("banana"))) # True
print("{} that 'pineapple' there is more than 1 'a|A'".format(repeating_letter_a("pineapple"))) # False
print("{} that 'Animal Kingdom' there is more than 1 'a|A'".format(repeating_letter_a("Animal Kingdom"))) # True
print("{} that 'A is for apple' there is more than 1 'a|A'".format(repeating_letter_a("A is for apple"))) # True


print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))

print(re.search(r"r\.com", "welcome"))

print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*", "And_this_is_anotther"))

print(re.search(r"\w \w", "123 Ready GO") != None)

print(re.search(r"\w \w", "username user_01") != None)

print(re.search(r"\w \w", "one") != None)

print(re.search(r"\w \w", "shopping_list: milk, bread, eggs.") != None)

#### match whole word ###
print(re.search(r"^A.*a$", "Argentina"))

# re.search(r"A.*a", "Azerbaijan") ===> 'Azerbaija'
print(re.search(r"^A.*a$", "Azerbaijan"))

# patern if a variable is valid
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_var"))

print(re.search(pattern, "this isnt a_valid_var"))

print(re.search(pattern, "this_is_a_valid_var2"))

print(re.search(pattern, "2this_is_a_valid_var"))

pattern = r"^[a-zA-Z0-9][\w\.\+\-]*\.[a-zA-Z]+$"

print(re.search(pattern, "gmail.com")) # True
print(re.search(pattern, "www@google")) # False
print(re.search(pattern, "www.Coursera.org")) # True
print(re.search(pattern, "web-address.com/homepage")) # False
print(re.search(pattern, "My_Favorite-Blog.US")) # True

pattern = r"^[0-1]?[0-9]\:[0-5][0-9] ?[a|A|p|P][M|m]"

print(re.search(pattern,"12:45pm")) # True
print(re.search(pattern,"9:59 AM")) # True
print(re.search(pattern,"6:60am")) # False
print(re.search(pattern,"five o'clock")) # False
print(re.search(pattern,"10:45pm")) # True
print(re.search(pattern,"06:00am")) # False


pattern = r".+ \d{5}(?:-\d{4})?[ \.\?\!\)]"

print(re.search(pattern,"ork are 10001 thru 11104.")) # True
print(re.search(pattern,"own, AZ 85258-0001.")) # True
print(re.search(pattern,"AZ 85258-00.")) # False

print(re.search(pattern,"ork are 100017 ")) # False':w


