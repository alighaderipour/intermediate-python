xyz = []
# generator => generates a stream in range of 0 to 5 | doesn't store in memory abit slower (less memory usage)
for i in range(5):
    xyz.append(i)
print("first  xyz {}".format(xyz))




# list comprehension => list stores in memory and faster
xyz = [i for i in range(5)]
print("second xyz {}".format(xyz))



# generator expressions
# doesn't store in memory but it's a generator expression
xyz = (i for i in range(5))
for i in xyz:
    print(i)

 
xyz = [i for i in range(5)]
print("second xyz {}".format(xyz))


