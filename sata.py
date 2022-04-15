
def numToCons(n):
    r = ''
    for nc in n:
        match nc:
            case '0': r += 'l'
            case '1': r += 'j'
            case '2': r += 'n'           
            case '3': r += 'm'
            case '4': r += 'k'
            case '5': r += 's'
            case '6': r += 'h'
            case '7': r += 't'
            case '8': r += 'r'
            case '9': r += 'p'
    return r

for n in range(100):
    zp = f'{n:02}'
    print('%s %s ' %(zp, numToCons(zp)))