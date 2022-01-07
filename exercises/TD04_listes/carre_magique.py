L = [0] * 4
for i in range(4) : # pour chaque ligne
    L[i] = [0] * i + [1] + [2] * (4 - i - 1)

for i in L:
    print(' '.join([str(j) for j in i]))

