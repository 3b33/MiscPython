from pprint import pprint

# add HFrame
part = {
    'Motor': {
        'Rotor': 1, 
        'Stator': 1
    },
    'EIBeam': {
        'SBeam': 4,
        'Con': 5
    },
    'ACU': {
        'AWiring': 15,
        'Circuit': 10,
        'HFrame': 2,
        'Computer': 2
    },
    'MEngine': {
        'Motor': 2,
        'Rubber': 15,
        'SPlate': 2
    },
    'VFrame': {
        'MFrame': 1,
        'SBeam': 1
    },
    'SPlating': {
        'RIPlate': 1,
        'Rotor': 1
    },
    'AWiring': {
        'Stator': 1,
        'Cable': 20 # ?
    },
    'Stator': {
        'SPipe': 3,
        'Wire': 8
    },
    'Rotor': {
        'Rod': 5,
        'Screw': 25
    },
    'RIPlate': {
        'Plate': 6,
        'Screw': 12
    },
    'MFrame': {
        'RIPlate': 3,
        'Rod': 12
    },
    'Computer': {
        'Circuit': 10,
        'Cable': 9,
        'Plastic': 18,
        'Screw': 52
    },
    'Circuit': {
        'CSheet': 2,
        'Plastic': 4
    },
    'HFrame': {
        'MFrame': 5,
        'Spipe' : 15,
        'EIBeam': 5,
        'Screw': 100
    }
}

print('blaa' * 5)

def dive(d, v, l):
    print('%s%s' % ('- ' * (l-1), d))
    if d in part:
        for dp in part[d]:
            dive(dp, part[d][dp] * v, l+1)
    else:
        if d in total:
            total[d] += v
        else:
            total[d] = v


total = {}
pprint(part.keys())
p = input('Part: ')
n = int(input('#: '))
if p in part:
    dive(p, n, 1)
    pprint(total)
else:
    print('what\'s that')

