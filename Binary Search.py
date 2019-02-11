data = [1,2,3,4,4,5,6,7,7,8,9,13]
target = 14

#linear search
def linear_search(data,target):
    for i in range(len(data)):
        if data[i]==target:
            return True
    return False

# find = linear_search(data,target)
# print(find)

#iterative binary search
def itertative_binary_search(data,target):
    low = 0
    high = len(data)-1


    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# find = itertative_binary_search(data,target)
# print(find)

#Recursive binary search
def recursive_binary_search(target, data, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return recursive_binary_search(target,data,low,mid-1)
        else:
            return recursive_binary_search(target,data,mid+1,high)



find = recursive_binary_search(target,data,0,len(data)-1)
print(find)
