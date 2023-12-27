from pprint import pprint
from random import randint

def numToCons(n):
    r = ''
    for nc in n:
        match nc:
            case '0': r += 'N'  # was L
            case '1': r += 'L'  # was J
            case '2': r += 'V'  # was N           
            case '3': r += 'M'
            case '4': r += 'K'
            case '5': r += 'S'
            case '6': r += 'H'
            case '7': r += 'T'
            case '8': r += 'R'
            case '9': r += 'P'
    return r

# copy from drive Sata doc, not in git.
sata_txt = open('sata.txt', 'r', encoding='ISO-8859-1')
sata = {}
for row in sata_txt:
    row = row.rstrip('\n')
    row_list = row.split(', ')
    number = row_list[0][:2]
    person = row_list[0][6:]
    items = row_list[1:]
    sata[number] = {}
    sata[number]['person'] = person
    sata[number]['items'] = items
sata_txt.close()

#for n in range(100):
#    zp = f'{n:02}'
#    print('%s %s' %(zp, numToCons(zp)))

#pprint(sata)

print('enter = quit\n')
correct = 0
all = 0

while 1:
    question = str(randint(0,10000)).zfill(4)
    inp = input('%s: ' % question)
    if inp == '': break
    number1 = question[:2]
    number2 = question[2:]
    print('%s %s' % (sata[number1]['person'], sata[number2]['items'][0]))
    if len(sata[number2]['items']) > 1: print(sata[number2]['items'][1])
    if sata[number1]['person'] in inp:
        print('Hyvä!!')
        correct += 1
    all += 1
    print('%s/%s %s%' % (correct, all, round(correct/all*100,0)))
    print()