import os
os.system('cls' if os.name == 'nt' else 'clear')

def say_hello(name, age, height):
    return "{} is {} years old with height {}".format(name, age , height)

p1 = {"name": "ali", "age":21 , "height":176}
print(say_hello(**p1))