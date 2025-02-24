names = ["Ali", "Reza", "Zahra", "Sue"]

for name in names:
    print('Hello, '+ name)
    print(' '.join(['Hello,',name]))

print(', '.join(names))


location_of_files ='D:\Ali Ghaderipour\courses\Workspace\Python\intermediate-python'
file_name='example.txt'

print(location_of_files+ '\\' + file_name)

import os
with open(os.path.join(location_of_files, file_name)) as d:
    print(d.read())

who = 'Gary'
how_many = 12
# Gary bought 12 apples today!
print(who,'bought',how_many,'apples today!') # bad way
print('{0} bought {1} apples today!'.format(who, how_many)) # python2 (outdated)
print('{} bought {} apples today!'.format(who, how_many)) # correct way in python3


# so the correct way is string formatting with {}
names = ["Ali", "Reza", "Zahra", "Sue"]
for name in names:
    print('Hello, {}'.format(name))
