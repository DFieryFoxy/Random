import csv

name = input("What's your name? ")
home = input("Where's your home? ")
house = input("Which is your house? ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home", "house"])
    writer.writerow({"name":name,"home": home,"house": house})
