# enumerate => returns a tuble containing basically the count along the way and the object itself ( or the item )
# that you iterate over soooo you use enumrate on iterable

example = ['lefet' , 'right', 'up', 'down']

for i in range(len(example)):
    print(i , example[i])


# everytime you need to do " for i in range (len something)" you are probably doing it wrong
print('---------------------------------enumerate-----------------------------------------')
for i, j in enumerate(example):
    print(i, j)

print('---------------------------------enumerate on dict-----------------------------------------')
# you can use enumrate over any iterable

my_dict = dict(enumerate(example))
print(my_dict)


[print(i,j) for i, j in my_dict.items()]
#--------------------- another example

import random
ml = [random.randint(1,100) for i in range(100)]
enum1 = ([i , j] for i , j in enumerate(ml) if i%2 ==0 )
for i in enum1:
    print(i)