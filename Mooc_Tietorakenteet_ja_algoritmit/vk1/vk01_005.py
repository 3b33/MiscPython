'''
Tehtäväsi on muodostaa n × n -ruudukko, jonka vasemmassa yläkulmassa on luku 0 ja kaikissa muissa ruuduissa on pienin epänegatiivinen kokonaisluku, jota ei esiinny vasemmalla samalla rivillä eikä ylhäällä samassa sarakkeessa.

Tee luokka Ruudukko, jossa on seuraavat metodit:

int[][] muodosta(int n): palauttaa ruudukon sisällön
Rajat:

1 ≤ n ≤ 50
Seuraava koodi esittelee luokan käyttämistä:

int n = 5;
Ruudukko r = new Ruudukko();
int[][] u = r.muodosta(n);
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        System.out.print(u[i][j]+" ");
    }
    System.out.println();
}

Koodin tulostuksen tulisi olla seuraava:

0 1 2 3 4
1 0 3 2 5
2 3 0 1 6
3 2 1 0 7
4 5 6 7 0
'''

import math
import time

print('\n')

debug = 0

tests = [5,50]
if debug: tests = [tests[0]]


def maxIntGrid(n):
    grid = []
    for y in range(n):
        grid.append([])
        if debug: print(grid)
        for x in range(n):
            col = []
            if y > 0:
                if debug: print(x,y)
                for row in grid[:-1]: col.append(row[x])
            new = 0
            while new in (grid[y] + col): new += 1
            grid[y].append(new)
    return grid


def printList(g):
    for y in g: print(*y)


print('\n')
for test in tests:
    startTime = time.time()
    printList(maxIntGrid(test))
    print('%ss\n' % round(time.time()-startTime,4))
print('\n')