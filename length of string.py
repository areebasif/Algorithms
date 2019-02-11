str1 = 'areeb asif'
#iteration
def length_of_string_iter(str):
    count = 0
    for item in str:
        count = count+1
    return count

print(length_of_string_iter(str1))

#recursion
def length_of_string_rec(str):
    if str == '':
        return 0
    return 1 + length_of_string_rec(str[1:])


print(length_of_string_rec(str1))