import os
os.system('cls' if os.name == 'nt' else 'clear')

combo_point = (8, 3, 2, 4)
flag = False
for c1 in range(10):
    if flag:
        break
    for c2 in range(10):
        if flag:
            break
        for c3 in range(10):
            if flag:
                break
            for c4 in range(10):
                if flag:
                    break
                print((c1, c2, c3, c4))               
                if (c1, c2, c3, c4) ==combo_point:
                    print('combo was found {}'.format((c1, c2, c3, c4)))
                    flag = True
                
                
                   
                