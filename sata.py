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
    if row != '':
        row_list = row.split(', ')
        number = row_list[0][:2]
        person = row_list[0][6:].split(' (')[0]  # some have explainers like (himym) or (f1)
        items = row_list[1:]
        sata[number] = {}
        sata[number]['person'] = person
        sata[number]['items'] = items
sata_txt.close()

#for n in range(100):
#    zp = f'{n:02}'
#    print('%s %s' %(zp, numToCons(zp)))

#pprint(sata)

randints = [x for x in range(100)]
while randints != []:
    i = randint(0, len(randints) - 1)
    print(str(randints[i]).zfill(2) + ' ')
    randints.pop(i)
quit()


print('q = quit\n')
answers = []
hint = ''
mods = ['', 'q']

while 1:
    if hint == '':
        question = str(randint(0,10000)).zfill(4)
    inp = input('%s: ' % question)
    if inp == '':   # give a hint
        number1 = question[:2]
        if hint == '':
            person = sata[number1]['person']
            first_name = person.split(' ')[0]
            last_name = person.split(' ')[1]
            hint = '%s%s %s%s' % (first_name[0], '.' * (len(first_name) - 1), last_name[0], '.' * (len(last_name) - 1))
            print(hint)
            continue
        elif '.' in hint:
            person_l = list(sata[number1]['person'])
            hint_l = list(hint)
            hidden = hint.count('.')
            while hint.count('.') == hidden:
                new_hint_pos = randint(0,len(hint_l) - 1)
                hint_l[new_hint_pos] = person_l[new_hint_pos]
                hint = ''.join(hint_l)
            print(hint)
            continue
        continue
    number1 = question[:2]
    number2 = question[2:]
    print('%s %s' % (sata[number1]['person'], sata[number2]['items'][0]))
    if len(sata[number2]['items']) > 1: print(sata[number2]['items'][1])
    if sata[number1]['person'].lower() in inp.lower() and hint == '':
        print('Hyvä!!')
        answers.append(1)
        if len(answers) == 10: print('Läpi meni!!!')
    elif inp != 'q':
        if '(' in sata[number1]['person']:
            print(sata[number1])
        if hint == '':
            print('Feilure...')
            print()
            answers = []
            continue
        elif answers != []:
            answers.pop(0)
    # if len(answers) > 10: answers.pop(0)
    #print('%s/%s %d%' % (answers.count(1), len(answers), round(answers.count(1)/len(answers)*100)))
    if '2' in question and inp not in mods and 'v' not in inp.lower():
        print('!!! N = V !!!')
    print(len(answers)) # this turned into 'correct answers'
    print()
    hint = ''
    if inp == 'q': break