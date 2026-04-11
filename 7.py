n = int(input())
i = 1
sonlar = []
while i <= n:
    son = input()
    sonlar.append(son)
    i += 1

print(sonlar[-2], sonlar[-1])