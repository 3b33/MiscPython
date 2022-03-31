# add HFrame
part = {
    'Motor': {
        'Rotor': 1, 
        'Stator': 1
    },
    'EBeam': {
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
        'Nails': 25
    },
    'RIPlate': {
        'Plate': 6,
        'Nails': 12
    },
    'MFrame': {
        'RIPlate': 3,
        'Rod': 12
    },
    'Computer': {
        'Circuit': 10,
        'Cable': 9,
        'Plastic': 18,
        'Nails': 52
    },
    'Circuit': {
        'CSheet': 2,
        'Plastic': 4
    }
}


def dive(d, v):
    if d in part:
        for i in range(v):
            for dp in part[d]:
                #if dp 
                dive(dp, part[d][dp])
    else:
        return d, v

answer = {}
p = input('Part: ')
n = input('#: ')
if p in part:
    for pp in part[p]:
        print(dive(pp, part[p][pp]))

else:
    print('what\'s that')

