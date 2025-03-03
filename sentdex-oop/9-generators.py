import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------our generator-------------------------------
def simple_gen():
    yield 'oh'
    yield 'hello'
    yield 'there'

for i in simple_gen():
    print(i)

# ------------------------------------------for loop generator-------------------------------------
simple_list = ['oh', 'hello','there']
for i in simple_list:
    print(i)


# -------------------------------------------list comprehension------------------------------------
simple_list = ['oh', 'hello','there']
[print(i) for i in simple_list]