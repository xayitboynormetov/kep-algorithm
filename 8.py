def reverse_number(number):
    str_number = str(number)
    return int(str_number[::-1])

n = input()
count = 0
for i in reverse_number(n):
    if i == '0':
        count += 1
    else:
        break
    
print(count)

