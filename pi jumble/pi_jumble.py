from mpmath import mp
from PIL import Image, ImageColor
from datetime import datetime

height = 200
width = 200
mp.dps = (height + width)
piString = str(mp.pi)
piString = piString.replace('.', '')
pia = [int(x) for x in piString]

print(''.join([str(x) for x in pia[:width]]))
listList = [pia]
for i in range(height):
    thisRow = []
    for di in range(len(listList[-1])-1):
        if di == 0:
            thisRow.append(3)
            continue
        prevIsEven = listList[-1][di-1] % 2 == 0
        nextIsEven = listList[-1][di+1] % 2 == 0
        same = listList[-1][di]
        minus = same - 1
        plus = same + 1
        if plus == 10: plus = 0
        if minus == -1: minus = 9
        if not prevIsEven and nextIsEven: thisRow.append(plus)
        elif prevIsEven and not nextIsEven: thisRow.append(minus)
        else: thisRow.append(same)
    #print(''.join([str(x) for x in thisRow[:width]]))
    listList.append(thisRow)

print('')

if 0:
    for row in listList:
        oddEvenList = []
        for d in row:
            #if d == 0: oddEvenList.append('#')
            if d % 2 == 0: oddEvenList.append('#')
            else: oddEvenList.append(' ')
        print(''.join(oddEvenList[:width]))

timestamp = str(datetime.now()).replace(':', '.')

im = Image.new('1', (width,height))
for y in range(height):
    row = listList[y]
    for x in range(width):
        if row[x] % 2 == 0:
            im.putpixel((x,y), (1))

print(len(listList))

im.save('pi jumble/images//Pi Jumble %s.png' % timestamp)