import os
os.system('cls' if os.name == 'nt' else 'clear')

correct_combo = (8, 3, 4, 1)
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                for c4 in range(10):
                    yield (c1, c2, c3, c4)


for c1, c2 , c3 , c4 in combo_gen():
    print(c1, c2, c3 ,c4)
    if (c1, c2, c3 ,c4 ) == correct_combo:
        print("combo was found".format((c1, c2, c3 ,c4)))
        break