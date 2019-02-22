def search(data, target):
    low = 0
    high = len(data)

    while high >= low:
        mid = (high+low)//2
        if data[mid] == target:
            if data[mid-1] == data[mid]:
                 high = mid -1
            else:
                return mid

        elif target < data[mid]:
            high = mid - 1 if mid-1 >0 else float('-inf')

        elif target > data[mid]:
            low = mid + 1 if mid+1 < len(data) else float('inf')

data = [-14,-14,-14,-10,2,108,108,243,285,285,285,401]
target = -14

print(search(data,target))


