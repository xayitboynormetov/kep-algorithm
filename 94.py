# 1. raqamlar yigindisi topuvchi funksiya
# 2. raqamlar kopaytmasini topuvchu funksiya
# 3. 100,1000 gacha bo'lgan tub sonlarkerak, har bir sonni p s ga qoldiqsiz bolinadiganni chiqaring
# def raqamlar_yigindisi(n):
#     s = 0
#     for i in str(n):
#         s += int(i)
#     return s
 

# def raqamlar_kopaytmasi(n):
#     s = 1
#     for i in str(n):
#         s *= int(i)
#     return s
# for n in range(100, 1000):
#     if raqamlar_kopaytmasi(n) % raqamlar_yigindisi(n) == 0:
#         print(n)

# 2 - usul
def raqamlar_yigindisi_kopaytmasi(n):
    s, p  = 0, 1
    for i in str(n):
        s += int(i)
        p *= int(i)
    return s, p
for n in range(100, 1000):
    s, p = raqamlar_yigindisi_kopaytmasi
    if p % s == 0:
        print(n)