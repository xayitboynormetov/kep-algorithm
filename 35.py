a = int(input())
b = int(input())
if a > b:
    a,b = b,a
s = 0
for n in range(a, b + 1):
    if n % 4 == 0:
        s += 1
print(s)