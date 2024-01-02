from random import random

arr = list(range(1, 45+1))

for i in range(1000):
    rnd = int(random()*45)
    tmp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = tmp 

for i in range(6):
    print(arr[i])