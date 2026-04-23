def sum_digits(number):
    s = 0
    for digit in str(number):
         raqam = int(digit)
         s += raqam
    
    return s

n = input()
n1 = n[0:3]
n2 = n[3:6]
if sum_digits(n1) == sum_digits(n2):
     print(True)
else:
     print(False)