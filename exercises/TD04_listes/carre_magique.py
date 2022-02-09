import random
def sudoku(): 
    l1 = [] 
    L = []
    while len(L)<4:
        a = random.randint(1,4)
        if a in L:
            continue
        else: 
            L.append(a)
    l1.append(L)
    L = []
    for i in range(3):
        while len(L)<4:
            a = random.randint(1,4)
            if a in L:
                continue
            else: 
                L.append(a)
                for j = i:
                    if L[j] == l1[i][j]:
                        L.remove(a)
        l1.append(L)
        L = []
    print(l1)
sudoku()