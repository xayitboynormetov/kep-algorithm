n = int(input())
a = list(map(int, input().split()))

for son in a:
    if son % 2 == 0:
        print(son, end=" ")