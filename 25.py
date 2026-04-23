import math

a = int(input())
b = int(input())
D = a**2 - b*4
x = (a + math.sqrt(D)) / 2
y = (b - math.sqrt(D)) / 2
print(x, y)