def max_2(*args):
    numbers = list(args)
    numbers.sort(reverse=True)
    return numbers[1]
print(max_2(2, -3, 5, 7))