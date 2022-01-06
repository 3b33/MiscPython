from mpmath import mp

mp.dps = 500
piString = str(mp.pi)
piString = piString.replace('.', '')
pia = [int(x) for x in piString]

print(''.join([str(x) for x in pia[:178]]))
listList = [pia]
for i in range(400):
    thisRow = []
    for di in range(len(listList[-1])-1):
        if di == 0:
            thisRow.append(3)
            continue
        prevIsEven = listList[-1][di-1] % 2 == 0
        nextIsEven = listList[-1][di+1] % 2 == 0
        if prevIsEven and nextIsEven: thisRow.append(listList[-1][di])
        elif prevIsEven or nextIsEven:
            plus = listList[-1][di] + 1
            if plus == 10: plus = 0
            thisRow.append(plus)
        else:
            minus = listList[-1][di] - 1
            if minus == -1: minus = 9
            thisRow.append(minus)
    #print(''.join([str(x) for x in thisRow[:178]]))
    listList.append(thisRow)

print('')

if 1:
    for row in listList:
        oddEvenList = []
        for d in row:
            #if d == 0: oddEvenList.append('#')
            if d % 2 == 0: oddEvenList.append('#')
            else: oddEvenList.append(' ')
        print(''.join(oddEvenList[:178]))