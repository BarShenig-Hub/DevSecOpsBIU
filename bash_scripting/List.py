lst = [4, 65, 12, 87, 34, 567, 2435, 165, 134, 15, 782, 37]

max1_num = lst[0]
max2_num = lst[0]
for num in lst:
    if num > max1_num:
        max2_num = max1_num
        max1_num = num
    elif num > max2_num:
        max2_num = num
print(max2_num)
print(max1_num)
