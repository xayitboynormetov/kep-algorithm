# n = int(input())
# s = 0
# for son in range(1, n + 1):
#     s += son 

# print(s)

import math
n = int(input())
s = 0
for son in range(1, n + 1):
    s += int(math.sqrt(son)) 

print(s)
