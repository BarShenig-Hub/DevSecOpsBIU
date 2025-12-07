# This loop finds the highest and second-highest numbers in the list by updating them as it scans each element.

lst = [4, 65, 12, 87, 34, 567, 2435, 165, 134, 15, 782, 37]

highest = lst[0]
second = lst[0]
for num in lst:
    if num > highest:
        second = highest
        highest = num
    elif num > second:
        second = num
print("The second highest number in the list is:", second)
print("The highest number is:", highest)
