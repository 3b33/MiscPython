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
'''

import math

print('\n')

debug = 0

tests = [5]
if debug: tests = tests[0]

# arf I misread the assignment. The whole row and column should be considered.
def maxIntGrid(n):
    grid = []
    for y in range(n):
        grid.append([])
        for x in range(n):
            left = grid[y][x-1] if x > 0 else -1
            up = grid[y-1][x] if y > 0 else -1
            corner = grid[y-1][x-1] if x > 0 and y > 0 else -1
            new = 0
            while new in [left,up,corner]: new += 1
            grid[y].append(new)
    return grid

def printGrid(g):
    for y in g: print(y)

print('\n')
for test in tests:
    printGrid(maxIntGrid(test))