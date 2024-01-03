from pprint import pprint
from random import randint
import os.path
import json

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
        sata[number]['item'] = items[0].replace('?', '')
sata_txt.close()

#for n in range(100):
#    zp = f'{n:02}'
#    print('%s %s' %(zp, numToCons(zp)))

#pprint(sata)

# randints = [x for x in range(100)]
# while randints != []:
#     i = randint(0, len(randints) - 1)
#     print(str(randints[i]).zfill(2) + ' ')
#     randints.pop(i)
# quit()

if not os.path.isfile('sata_answers.json'):
    answers = {}
else:
    with open('sata_answers.json', 'r') as sata_answers:
        answers = json.load(sata_answers)

# todo: read anwers from json if it exists

def info():
    #print('%d numeroa arvattu' % len(answers.keys()))
    filled = 0
    correct = 0
    wrong = 0
    for answer in answers.keys():
        if 'person' in answers[answer]:
            filled += len(answers[answer]['person'])
            correct += answers[answer]['person'].count(1)
            wrong += answers[answer]['person'].count(0)
        if 'item' in answers[answer]:
            filled += len(answers[answer]['item'])
            correct += answers[answer]['item'].count(1)
            wrong += answers[answer]['item'].count(0)
    print('%d / 1000 (%d %%) täytetty' % (filled, round(filled/1000 * 100)))
    print('%d oikein, %d väärin' %(correct, wrong))

print('q = save and quit, s = save, enter = hint\n')
hint = ''
mods = ['', 'q', 's','info']    # all possible non-answer inputs

info()

while 1:
    if hint == '':
        looping = True
        while looping:
            if randint(0,1): mode = 'item'
            else: mode = 'person'
            chance = 100
            question = str(randint(0,99)).zfill(2)
            if question in answers:
                if mode in answers[question]:
                    chance = max(answers[question][mode].count(0) / len(answers[question][mode]) * 100, 1)
            rnd = randint(0,99)
            if rnd <= chance:
                looping = False
            print('dev: chance for %s %s was %d %%' % (mode, question, chance))
        if question not in answers:
            print('First question for %s' % question)
        elif mode not in answers[question]:
            print('First %s question for %s' %(mode, question))
        else:
            print(answers[question][mode])
    inp = input('%s %s: ' % (mode.title(), question))
    if inp == '':   # give a hint
        if hint == '':
            if mode == 'person':
                person = sata[question]['person']
                first_name = person.split(' ')[0]
                last_name = person.split(' ')[1]
                hint = '%s%s %s%s' % (first_name[0], '.' * (len(first_name) - 1), last_name[0], '.' * (len(last_name) - 1))
            else: 
                item = sata[question]['item']
                hint = '%s%s' % (item[0], '.' * (len(item) - 1))
            print(hint)
            continue
        elif '.' in hint:
            if mode == 'person': correct_l = list(sata[question]['person'])
            else: correct_l = list(sata[question]['item'])
            hint_l = list(hint)
            hidden = hint.count('.')
            while hint.count('.') == hidden:
                new_hint_pos = randint(0,len(hint_l) - 1)
                hint_l[new_hint_pos] = correct_l[new_hint_pos]
                hint = ''.join(hint_l)
            print(hint)
            continue
        continue
    if inp not in mods:
        if question not in answers: answers[question] = {}
        if mode not in answers[question]: answers[question][mode] = []
        if sata[question][mode].lower() in inp.lower() and hint == '':
            print('Hyvä!!')
            answers[question][mode].append(1)
        else:
            if '(' in sata[question][mode]:
                print(sata[question])
            if hint == '':
                print('Feilure...')
            answers[question][mode].append(0)
        if len(answers[question][mode]) > 5: answers[question][mode].pop(0)
        if '2' in question and inp not in mods and 'v' not in inp.lower(): print('!!! N = V !!!')
        if question in answers and mode in answers[question]:
            print('%d %% oikein' % round(answers[question][mode].count(1) / len(answers[question][mode]) * 100))
        hint = ''
        print(sata[question][mode])
        print()
    elif inp == 'q': break
    elif inp == 'info': # does not work
        info()
    with open('sata_answers.json', 'w') as sata_answers:
          sata_answers.write(json.dumps(answers, indent=4))

