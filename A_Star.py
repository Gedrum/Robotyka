import math;
import copy;
import sys;


#sys.setrecursionlimit(4000)
# możliwi rodzice, rodzic od :1-góry,2-prawej,3-dołu,4-lewej

punkt = (0, 0)
cel = (19, 19)
ListaO = [punkt];
przeszkoda = 5
h = 0
f = 0


def wys(grid):
    for i in range(len(grid)):
        print(grid[i])
    print();

with open('grid.txt', 'r') as plik:
    grid = [[int(num) for num in line.split()] for line in plik]
#wys(grid);

listaO = copy.deepcopy(grid)
listaZ = copy.deepcopy(grid)
listaR = copy.deepcopy(grid)
kroki = copy.deepcopy(grid)
wyniki = copy.deepcopy(grid)

def wroc(start, punkt):
    wstaw(grid, punkt, 3)
    droga = [punkt]
    while (punkt != start):
        if (listaR[punkt[0]][punkt[1]] == 3):
            punkt = (punkt[0] + 1, punkt[1])
            wstaw(grid, punkt, 3)
            droga.append(punkt);
        elif (listaR[punkt[0]][punkt[1]] == 4):
            punkt = (punkt[0], punkt[1] - 1)
            wstaw(grid, punkt, 3)
            droga.append(punkt);
        elif (listaR[punkt[0]][punkt[1]] == 1):
            punkt = (punkt[0] - 1, punkt[1])
            wstaw(grid, punkt, 3)
            droga.append(punkt);
        elif (listaR[punkt[0]][punkt[1]] == 2):
            punkt = (punkt[0], punkt[1] + 1)
            wstaw(grid, punkt, 3)
            droga.append(punkt);
    wys(grid)
    print("Droga od punktu startu do punktu celu:\n",droga[::-1])

def krok(start, punkt):
    krok = 0
    while (punkt != start):
        if (listaR[punkt[0]][punkt[1]] == 3):
            punkt = (punkt[0] + 1, punkt[1])
            krok += 1
        elif (listaR[punkt[0]][punkt[1]] == 4):
            punkt = (punkt[0], punkt[1] - 1)
            krok += 1
        elif (listaR[punkt[0]][punkt[1]] == 1):
            punkt = (punkt[0] - 1, punkt[1])
            krok += 1
        elif (listaR[punkt[0]][punkt[1]] == 2):
            punkt = (punkt[0], punkt[1] + 1)
            krok += 1
    return krok

def wstaw(grid, punkt, wartosc):
    if (grid[punkt[0]][punkt[1]] != przeszkoda):
        grid[punkt[0]][punkt[1]] = wartosc

def minimum(grid):
    min = len(grid) * len(grid[0])
    g = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tmp = grid[i][j]
            if (tmp < min and grid[i][j] != 0 and grid[i][j] != przeszkoda and listaZ[i][j] != 1):
                min = tmp
                g = (i, j)
    return g

def heurystyka(start, punkt, cel):
    h = round(krok(start, punkt) + math.sqrt((punkt[0] - cel[0]) ** 2 + (punkt[1] - cel[1]) ** 2), 2)
    return (h)

def gora(grid, start, punkt, cel):
    punkt = (punkt[0] - 1, punkt[1])
    if ((punkt[0] >= 0 and punkt[1] >= 0) and (punkt[0] <= len(grid) - 1 and punkt[1] <= len(grid[0]) - 1)):
        if (grid[punkt[0]][punkt[1]] != przeszkoda):
            if (punkt == cel):
                wstaw(wyniki, punkt, 1)
                wstaw(listaR, punkt, 3)
            elif (listaO[punkt[0]][punkt[1]] == 0 and listaZ[punkt[0]][punkt[1]] != 1):
                wstaw(listaO, punkt, 1)
                ListaO.append(punkt)
                wstaw(listaR, punkt, 3)
                f = heurystyka(start, punkt, cel)
                wstaw(wyniki, punkt, f)
            elif (listaO[punkt[0]][punkt[1]] == 1 and listaZ[punkt[0]][punkt[1]] != 1):
                f = heurystyka(start, punkt, cel)
                if (f < wyniki[punkt[0]][punkt[1]]):
                    wstaw(listaR, punkt, 3)
                    wyniki[punkt[0]][punkt[1]] = f

def prawa(grid, start, punkt, cel):
    punkt = (punkt[0], punkt[1] + 1)
    if ((punkt[0] >= 0 and punkt[1] >= 0) and (punkt[0] <= len(grid) - 1 and punkt[1] <= len(grid[0]) - 1)):
        if (grid[punkt[0]][punkt[1]] != przeszkoda):
            if (punkt == cel):
                wstaw(wyniki, punkt, 1)
                wstaw(listaR, punkt, 4)
            elif (listaO[punkt[0]][punkt[1]] == 0 and listaZ[punkt[0]][punkt[1]] != 1):
                wstaw(listaO, punkt, 1)
                ListaO.append(punkt)
                wstaw(listaR, punkt, 4)
                f = heurystyka(start, punkt, cel)
                wstaw(wyniki, punkt, f)
            elif (listaO[punkt[0]][punkt[1]] == 1 and listaZ[punkt[0]][punkt[1]] != 1):
                f = heurystyka(start, punkt, cel)
                if (f < wyniki[punkt[0]][punkt[1]]):
                    wstaw(listaR, punkt, 4)
                    wyniki[punkt[0]][punkt[1]] = f

def dol(grid, start, punkt, cel):
    punkt = (punkt[0] + 1, punkt[1])
    if ((punkt[0] >= 0 and punkt[1] >= 0) and (punkt[0] <= len(grid) - 1 and punkt[1] <= len(grid[0]) - 1)):
        if (grid[punkt[0]][punkt[1]] != przeszkoda):
            if (punkt == cel):
                wstaw(wyniki, punkt, 1)
                wstaw(listaR, punkt, 1)
            elif (listaO[punkt[0]][punkt[1]] == 0 and listaZ[punkt[0]][punkt[1]] != 1):
                wstaw(listaO, punkt, 1)
                ListaO.append(punkt)
                wstaw(listaR, punkt, 1)
                f = heurystyka(start, punkt, cel)
                wstaw(wyniki, punkt, f)
            elif (listaO[punkt[0]][punkt[1]] == 1 and listaZ[punkt[0]][punkt[1]] != 1):
                f = heurystyka(start, punkt, cel)
                if (f < wyniki[punkt[0]][punkt[1]]):
                    wstaw(listaR, punkt, 1)
                    wyniki[punkt[0]][punkt[1]] = f

def lewa(grid, start, punkt, cel):
    punkt = (punkt[0], punkt[1] - 1)
    if ((punkt[0] >= 0 and punkt[1] >= 0) and (punkt[0] <= len(grid) - 1 and punkt[1] <= len(grid[0]) - 1)):
        if (grid[punkt[0]][punkt[1]] != przeszkoda):
            if (punkt == cel):
                wstaw(wyniki, punkt, 1)
                wstaw(listaR, punkt, 2)
            elif (listaO[punkt[0]][punkt[1]] == 0 and listaZ[punkt[0]][punkt[1]] != 1):
                wstaw(listaO, punkt, 1)
                ListaO.append(punkt)
                wstaw(listaR, punkt, 2)
                f = heurystyka(start, punkt, cel)
                wstaw(wyniki, punkt, f)
            elif (listaO[punkt[0]][punkt[1]] == 1 and listaZ[punkt[0]][punkt[1]] != 1):
                f = heurystyka(start, punkt, cel)
                if (f < wyniki[punkt[0]][punkt[1]]):
                    wstaw(listaR, punkt, 2)
                    wyniki[punkt[0]][punkt[1]] = f

def ruch(grid, start, punkt, cel):
    listaZ[punkt[0]][punkt[1]] = 1
    ListaO.pop(ListaO.index(punkt));

    gora(grid, start, punkt, cel)
    prawa(grid, start, punkt, cel)
    dol(grid, start, punkt, cel)
    lewa(grid, start, punkt, cel)

    p = minimum(wyniki)
    punkt = p
    # print(p)
    # wstaw(grid,punkt,3);
    # wys(grid); #agent znajduje się w miejscu w którym jest 3
    # wstaw(grid,punkt,0)
    wstaw(listaO, punkt, 0)
    # wys(listaO)
    if (punkt == cel):
        print("agent dotarł do celu")
        punkt = cel
        wroc(start, punkt)
    elif (len(ListaO) == 0):
        print("agent nie ma już dostępnych pól do ekspansji, nie jest w stanie dojść do celu")
    else:
        ruch(grid, start, punkt, cel)

ruch(grid, punkt, punkt, cel)
