lst = [4, 65, 12, 87, 34, 567, 2435, 165, 134, 15, 782, 37]

highest = lst[0]
second = lst[0]
for num in lst:
    if num > highest:
        second = highest
        highest = num
    elif num > second:
        second = num
print(second)
print(highest)
