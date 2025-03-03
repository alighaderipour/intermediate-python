import timeit
# print(timeit.timeit('1+3', number=500000000))


# input_list = range(100)

# def div_by_five(number):
#     if number %5 == 0:
#         return True
#     return False

# xyz = (i for i in input_list if div_by_five(i))

# xyz = [i for i in input_list if div_by_five(i)]

# xyz = list (i for i in input_list if div_by_five(i))

# xyz = list ((i for i in input_list if div_by_five(i)))
print(timeit.timeit
("""
input_list = range(100)
def div_by_five(number):
    if number %5 == 0:
        return True
    return False
xyz = (i for i in input_list if div_by_five(i))
"""
, number = 500000)) # 10.368022917999951


print(timeit.timeit("""
input_list = range(100)
def div_by_five(number):
    if number %5 == 0:
        return True
    return False
xyz = [i for i in input_list if div_by_five(i)]"""
, number=500000 ))



print(timeit.timeit("""
input_list = range(100)
def div_by_five(number):
    if number %5 == 0:
        return True
    return False
xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
   x=i
"""
, number=500000 ))