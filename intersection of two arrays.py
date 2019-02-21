def intersec(arr1,arr2):
    i = 0
    j = 0
    lst = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:

            if arr1[i] not in lst:
                lst.append(arr1[i])
            i = i + 1
            j = j + 1

        elif arr1[i] > arr2[j]:
            j = j+1
            
        elif arr1[i] < arr2[j]:
            i = i+1
    return lst

A = [2,3,3,5,7,11]
B = [3,3,7,15,31]

print(intersec(A,B))