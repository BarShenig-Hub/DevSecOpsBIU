lst = [15 , 2 , 8, -4, 76, 3, 2, 1, 80,-3]
new_lst = []

list_size = len(lst)
while (len(lst) > 0):
    list_size = len(lst)
    current_min_index = 0
    lowest = lst[0]
    list_size = len(lst)
    for index in range(list_size):
        if lst[index] < lowest:
            lowest = lst[index]
            current_min_index = index
    new_lst.append(lowest)
    del lst[current_min_index]
    print(f"{str(lst):33} {lowest}")
print("New list is:", new_lst)


