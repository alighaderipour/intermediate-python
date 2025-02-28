import os
os.system('cls' if os.name == 'nt' else 'clear')
import random

items =  [random.randint(1,100) for items in range(20)]

for i in range(len(items)):
    print(items[i])
