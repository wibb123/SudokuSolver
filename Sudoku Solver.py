import numpy as np

N = {1,2,3,4,5,6,7,8,9}
# Define Set for each set
GN = np.array([[N.copy() for x in range(9)] for x in range(9)])
# Define Sudoku grid
G = np.array(
    [[0, 0, 3, 1, 0, 0, 7, 2, 0],
     [7, 0, 0, 0, 0, 0, 5, 0, 0],
     [0, 5, 0, 2, 4, 0, 0, 3, 0],
     [0, 0, 0, 7, 2, 0, 0, 0, 0],
     [0, 0, 6, 0, 0, 0, 8, 0, 0],
     [0, 0, 0, 0, 1, 4, 0, 0, 0],
     [0, 6, 0, 0, 9, 5, 0, 8, 0],
     [0, 0, 5, 0, 0, 0, 0, 0, 9],
     [0, 4, 9, 0, 0, 2, 6, 0, 0]])

# 100 iterations should be enough
for roll in range(100):
    # for each cell, check if it's the only number that can go there
    for i in range(9):
        for w in range(9):
            if G[i][w] == 0:
                for a in range(9):
                    r = G[i][a]
                    c = G[a][w]
                    if r != 0:
                        GN[i][w].discard(r)
                    if c != 0:
                        GN[i][w].discard(c)

                if i % 3 == 0:
                    i_2 = i
                elif i % 3 == 1:
                    i_2 = i - 1
                elif i % 3 == 2:
                    i_2 = i - 2
                if w % 3 == 0:
                    w_2 = w
                elif w % 3 == 1:
                    w_2 = w - 1
                elif w % 3 == 2:
                    w_2 = w - 2
                cellsG = np.array([G[i_2][w_2],
                                  G[i_2+1][w_2],
                                  G[i_2+2][w_2],
                                  G[i_2][w_2+1],
                                  G[i_2+1][w_2+1],
                                  G[i_2+2][w_2+1],
                                  G[i_2][w_2+2],
                                  G[i_2+1][w_2+2],
                                  G[i_2+2][w_2+2]])
                cellsGN = np.array([GN[i_2][w_2],
                                   GN[i_2 + 1][w_2],
                                   GN[i_2 + 2][w_2],
                                   GN[i_2][w_2 + 1],
                                   GN[i_2 + 1][w_2 + 1],
                                   GN[i_2 + 2][w_2 + 1],
                                   GN[i_2][w_2 + 2],
                                   GN[i_2 + 1][w_2 + 2],
                                   GN[i_2 + 2][w_2 + 2]])
                for a in range(9):
                    cell_a = cellsG[a]
                    if cell_a == G[i][w]:
                        continue
                    GN[i][w].discard(cell_a)
                if len(GN[i][w]) == 1:
                    for a in GN[i][w]:
                        G[i][w] = a
                if len(GN[i][w]) == 2:
                    for a in range(9):
                        if a == i:
                            continue
                        elif GN[i][w] == GN[a][w]:
                            for q in range(9):
                                if q == a or q == i:
                                    continue
                                else:
                                    for d in GN[i][w]:
                                        GN[q][w].discard(d)
                    for a in range(9):
                        if a == w:
                            continue
                        elif GN[i][w] == GN[i][a]:
                            for q in range(9):
                                if q == a or q == w:
                                    continue
                                else:
                                    for d in GN[i][w]:
                                        GN[i][q].discard(d)
                    for a in range(9):
                        if cellsG[a] == G[i][w]:
                            continue
                        elif GN[i][w] == cellsGN[a]:
                            for q in range(9):
                                if q == a or cellsG[q] == G[i][w]:
                                    continue
                                else:
                                    for d in GN[i][w]:
                                        cellsGN[q].discard(d)

            else:
                GN[i][w] = {G[i][w]}
    # for every digit, check if it only has 1 option in each box/row/column
    for j in range(1,10):
        for k in range(9):
            x = 0
            for l in range(9):
                if j in GN[k][l]:
                    x = x + 1
                    col = l
            if x == 1:
                G[k][col] = j
        for k in range(9):
            x = 0
            for l in range(9):
                if j in GN[l][k]:
                    x = x + 1
                    row = l
            if x == 1:
                G[row][k] = j
        for k in range(3):
            for l in range(3):
                x = 0
                for n in range(3):
                    for m in range(3):
                        if j in GN[(3 * k) + n][(3 * l) + m]:
                            x = x + 1
                            row = (3 * k) + n
                            col = (3 * l) + m
                if x == 1:
                    G[row][col] = j
        for b in range(1,10):
            if j != b:
                double = {j,b}
                for k in range(3):
                    for l in range(3):
                        x = 0
                        y = 0
                        z = 0
                        rows = []
                        cols = []
                        for n in range(3):
                            for m in range(3):
                                if j in GN[(3 * k) + n][(3 * l) + m] and b in GN[(3 * k) + n][(3 * l) + m]:
                                    x = x + 1
                                    rows.append((3 * k) + n)
                                    cols.append((3 * l) + m)
                                if j in GN[(3 * k) + n][(3 * l) + m]:
                                    y = y + 1
                                if b in GN[(3 * k) + n][(3 * l) + m]:
                                    z = z + 1
                        if x == 2 and y == 2 and z == 2:
                            for a in range(2):
                                row = rows[a]
                                col = cols[a]
                                GN[row][col] = double.copy()
                for k in range(9):
                    x = 0
                    y = 0
                    z = 0
                    rows = []
                    for l in range(9):
                        if j in GN[l][k] and b in GN[l][k]:
                            x = x + 1
                            rows.append(l)
                        if j in GN[l][k]:
                            y = y + 1
                        if b in GN[l][k]:
                            z = z + 1
                    if x == 2 and y == 2 and z == 2:
                        for a in range(2):
                            row = rows[a]
                            GN[row][k] = double.copy()
                for k in range(9):
                    x = 0
                    y = 0
                    z = 0
                    cols = []
                    for l in range(9):
                        if j in GN[k][l] and b in GN[k][l]:
                            x = x + 1
                            cols.append(l)
                        if j in GN[k][l]:
                            y = y + 1
                        if b in GN[k][l]:
                            z = z + 1
                    if x == 2 and y == 2 and z == 2:
                        for a in range(2):
                            col = cols[a]
                            GN[k][col] = double.copy()
print(GN)
print(G)