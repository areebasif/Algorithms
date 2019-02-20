def int_to_string(number):
    if number < 0 :
       is_negative = True
       number = number * -1

    is_negative =   False

    lst = []
    while  number > 0:

        last_char = lst.append(chr(ord('0') + number%10 ))
        number = number//10

    lst = lst[::-1]
    out_string = ''.join(lst)

    if is_negative:
        return '-'+ out_string
    return out_string

print(int_to_string(123))
print(type(int_to_string(123)))