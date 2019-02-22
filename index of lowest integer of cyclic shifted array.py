def idx(data):
    low = 0
    high = len(data)-1
    while low<high:
        mid = (low+high)//2
        if data[mid]>data[high]:
            low = mid +1 if mid+1< len(data) else float ('inf')
        elif data[mid]<data[high]:
            high = mid if mid>0 else float ('-inf')
    return low

print(idx([2,3,4,5,6,7,1]))