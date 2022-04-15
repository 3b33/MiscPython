from random import randint

with open('two million rows.csv', 'w+') as f:
    f.write('Values\n')
    for n in range(2000000):
        f.write('%s\n' % randint(1,100))
