def fixed_point (data):
    low = 0
    high = len(data)-1

    if low == high:
        if data[low] == -1 or data[low] == 0:
            return data[low]



    while low<=high:
        mid = (high+low)//2

        if data[mid] < mid:
            low = mid + 1
        elif data[mid] > mid:
            high = mid - 1
        else:
            return data[mid]

    return None

print(fixed_point([2]))
