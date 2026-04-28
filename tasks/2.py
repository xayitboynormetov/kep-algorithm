lst = [18, 22, 5, 38, 0, 7]
sum = 0
for element in lst:
    if element < 30 and element % 3 == 0:
        print(element, end =" ")

    else:
        sum += element

print()
print(sum)


# for index in range(len(lst)): 
    # print(index, lst[index])