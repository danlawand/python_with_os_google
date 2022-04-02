#!/usr/bin/env python3

# Comma Separeted Values = CSV
import csv

f = open("csv_file.txt")

csv_f = csv.reader(f)

for row in csv_f:
    # cada valor separado por vírgula é atribuído a uma variável que representa
    # a sua coluna
    name, number, role = row
    print("Name: {}, Number: {}, Role: {}".format(name, number, role))

f.close()

print("----------------")
print()


hosts = [["workstation.local", "92.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    # Precisamos criar uma variável que possa fazer as operações de inserção no
    # arquivo
    # writer é uma instância de uma classe de escritor CSV
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
print("Generated hosts.csv file")


print("----------------")
print()

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["user"]))

print("----------------")
print()

users = [{"name": "Joao", "username": "jota"}, {"name": "Matias", "username":
    "amigao"}]

keys = ["name", "username"]

with open('name_username.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

print("name_usernam.csv file created")

