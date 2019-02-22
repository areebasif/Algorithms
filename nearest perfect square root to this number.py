def perfect_square_nearest_to_this(num):
    low = 0
    high = num
    while high>low:
        mid = (low + high)//2

        if mid**2 <= num:
            low = mid + 1
        else:
             high = mid - 1

    return low - 1



print(perfect_square_nearest_to_this(300))


