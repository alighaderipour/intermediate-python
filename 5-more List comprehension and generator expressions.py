"""
# a list
xyz = [i for i in range(5)]
print(xyz)

# a generator object
xyz =(i for i in range(5))
print(xyz)
"""

input_list = [45,3,74,127,87,56,30,65,45]

def div_by_five(num):
    if num%5==0:
        return True
    else:
        return False
# this xyz1 below is not a list ! it's a generator
xyz1 = (i for i in input_list if div_by_five(i))
# print(xyz1) you see it's a generator
"""
# xyz1 is kinda doing same as xyz2 even tho xyz1 is generator and xyz2 is a list 
xyz2 = []
for i in input_list:
    if div_by_five(i):
        xyz2.append(i)
"""
# we have to comment this for loop below in order to let [print(i) for i in xyz1] works why?
# cause When you iterate over a generator, it produces values one by one until it is exhausted.
# Once a generator is exhausted, it cannot produce any more values unless you create a new generator.
"""
for i in xyz1 :
    print(i)
"""
# instead of this for we can do this
[print(i) for i in xyz1]


# -------------------------------------------conclusion---------------------------------
xyz = (i for i in input_list if div_by_five(i))
print(xyz) # a generator with if which we iterate over and does not take alot space in memory but slower
[print(i, 'generator') for i in xyz]
xyz =[ i for i in input_list if div_by_five(i)]
print(xyz) # a list comprehension with if which stores in memory and faster but takes space in memory
[print(i, 'list') for i in xyz]



