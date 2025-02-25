xyz = []
for i in range(5):
    xyz.append(i)
print("first  xyz {}".format(xyz))




xyz = [i for i in range(5)]
print("second xyz {}".format(xyz))



# generator expressions
xyz = (i for i in range(5))
for i in xyz:
    print(i)