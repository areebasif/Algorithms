def bitonic_peak(data):
    low = 0
    high = len(data) - 1

    if len(data) < 3:
        return None

    while low <= high:
        mid =(low+high)//2

        mid_left = data[mid-1] if mid - 1 >=0 else float('-inf')
        mid_right = data[mid+1] if mid +1 < len(data) else float ('inf')

        if mid_left < data[mid] and mid_right > data[mid]:
            low = mid + 1

        elif mid_left > data[mid] and mid_right < data[mid]:
            high = mid - 1

        elif mid_left < data[mid] and mid_right < data[mid]:
            return data[mid]


print(bitonic_peak([1,2,3,4,1]))

