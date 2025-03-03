# the zip function takes elements from multiple iterable and aggregate them into one
# where we basically share the index value 
x = [1, 2, 3, 4]
y = [ False, True, True, False]
z = ['a', 'b', 'c', 'd']

# for i in zip(x, y, z):
#     print(i)


# for a, b, c in zip(x, y, z):
#     print(a, b, c)

# print(list(zip(x, y, z)))
# print([i for i in zip(x, y, z)])
# [print( a,b,c) for a,b,c in zip(x,y,z)]

# print([zip(x, y, z)])


# print(dict(zip(x,y)))


# ---------------------- in list comprehesnion x, y are temporary-----------------
# ---------------------- in for loop they are stored in memory so you can see x -----------------

[print(x, y) for x, y in zip(x,y)]
print(x) # you see original x list

for x, y in zip(x, y):
    print(x,y)
print(x) # you see only 4