# This code finds the highest number in the list and then moves it forward by swapping it with any smaller value that appears after it.

lst = [14, 15, 7, 10, 4, 2, 3]

highest = max(lst)
print("The highest number in the list is", highest)

index_of_highest = lst.index(highest)

for i in range(index_of_highest + 1, len(lst)):
    if highest > lst[i]:
        lst[lst.index(highest)] = lst[i]
        lst[i] = highest
        print(lst)


print("The new list is", lst) 
