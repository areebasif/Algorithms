str1 = 'AREEBasiF'
str2 = 'AreebAsif'
str3 = 'areebASIF'

#by iteration
def find_upper_case_iter(str: object) -> object:
    for i in range(len(str)):
        if str[i].isupper():
            return str[i]
    return("no uppercase found")

# print(find_upper_case_iter(str1))
# print(find_upper_case_iter(str2))
# print(find_upper_case_iter(str3))

#by recursion
def find_upper_case_rec(str,idx = 0):
    if str[idx].isupper():
        return str[idx]
    if idx == len(str)-1:
        return("no upper case found")
    return find_upper_case_rec(str, idx+1)

print(find_upper_case_rec(str1))
print(find_upper_case_rec(str2))
print(find_upper_case_rec(str3))
