# 1 - usul
def month_to_season(oy):
    if oy == 12 or oy == 1 or oy == 2:
        return 'Qish'
    elif oy == 3 or oy == 4 or oy == 5:
        return 'Bahor'
    elif oy == 6 or oy == 7 or oy == 8:
        return 'Yoz'
    elif oy == 9 or oy == 10 or oy == 11:
        return 'Kuz'

# 2 - usul
# def month_to_season(oy): 
#      if oy in [ 12, 1 ,2]:
#         return 'Qish'
#     elif oy in [3, 4, 5]:
#         return 'Bahor'
#     elif oy in [6, 7, 8]:
#         return 'Yoz'
#     elif oy in [9, 10, 11]:
#         return 'Kuz'