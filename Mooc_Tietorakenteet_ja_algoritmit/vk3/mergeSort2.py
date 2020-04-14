# https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a = mergeSort(a)
        b = mergeSort(b)
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
    return c

import random
import time

# driver code to test the above code 
arr = [random.randint(1,10**6) for x in range(10**5)]  
print ("Given array start is", end="\n")  
print(arr[:3])
startTime = time.time()
mergeSort(arr)
print(time.time()-startTime)
print("Sorted array start is: ", end="\n") 
print(arr[:3])

'''
Given array start is
[504092, 660213, 120370]
8.081182956695557s
Sorted array start is: 
[504092, 660213, 120370]
'''