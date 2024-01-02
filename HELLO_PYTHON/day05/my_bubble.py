arr = [5, 4, 3, 2, 1]

for i in range(5):
    for j in range(5):
        if arr[i] < arr[j]:
            #tmp = arr[i]
            #arr[i] = arr[j]
            #arr[j] = tmp  
            
            a = arr[i]
            b = arr[j]
            arr[i] = b
            arr[j] = a

print(arr)