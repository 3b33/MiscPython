import random

# aeiouy
def nameGen():
    name1 = ['Baa','Lof','Kel','Nau','Fos','A','No','Ui']
    name2 = ['ler','kos','maa','pes','fan','toe','bol','ka']
    return random.choice(name1)+random.choice(name2)

def main():
    ne = random.randrange(5)+1  # number of entities
    entities = []
    for x in range(ne):
        entities.append([nameGen()])

    startStr = 'In the beginning, there ' + ('is one' if ne == 1 else 'were '+ str(ne))  + ' entit'+ ('ies' if ne > 1 else 'y') + ' called '
    for x in range(ne):
        startStr += entities[x][0]
        if x < ne-2:
            startStr += ', '
        elif x == ne-2:
            startStr += ' and '
        else:
            startStr += '.'
            
    print(startStr)

main()

