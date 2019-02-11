def multi_by_recursion (x,y):

    if y==0:
        return 0
    return x +  multi_by_recursion(x,y-1)

print(multi_by_recursion(2,3))