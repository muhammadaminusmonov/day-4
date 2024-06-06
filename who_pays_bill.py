import random

names = input("Enter names to choose who is going to pay the bill for everyone: ")
list_names = names.split(" ")
print(f"{random.choice(list_names)} is going to pay the bill for everyone")