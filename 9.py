txt = 'abcd'
# print(txt[1 : 3])
# print(txt[0 : len(txt)])
# print(txt[0::])
# print(txt[::-1])

def reverse_number(number):
    str_number = str(number)
    return int(str_number[::-1])


for num in range(1000, 10000):
    reverse_num = reverse_number(num)
    if reverse_num == 4 * num:
        print (num)