# nested list comprehension
# [expression for item in iterable]

[[print(i, j ) for j in range(5)] for i in range(5)]

print ('same as below but backward')
for i in range(5):
    for j in range(5):
        print(i, j)

print('------x----')
xyz = [[(i, j) for j in range(5)] for i in range(5)]
print(xyz) # it's tuple


xyz = [[[i, j] for j in range(5)] for i in range(5)]
print(xyz) # it's list

# embed generator

xyz = ([[i, j] for j in range(5)] for i in range(5))
print(xyz) # it's generator expression

# you can iterate over a generator expression
print( [i for i in xyz])

# or print like this :
xyz = ([[i, j] for j in range(5)] for i in range(5))
for i in xyz:
    print(i)

# if you want a tuple
xyz = ([(i, j) for j in range(5)] for i in range(5))
for i in xyz:
    print(i)

# another way
xyz = (((i, j) for j in range(5)) for i in range(5))
for i in xyz:
    print(i)

## nested generators
xyz = (((i, j) for j in range(5)) for i in range(5))
for i in xyz:
   for ii in i:
    print(ii)

# what is the point of all of this?
# if we use generator expression you can run something like this
# at least your program won't crash
xyz = (((i, j) for j in range(500000000000000000)) for i in range(500000000000000000))
for i in xyz:
   for ii in i:
    print(ii)
# but if we use list comprehension we may run out of memory