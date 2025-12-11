# 0, 1, 1, 2, 3 , 5, 8, 13, 21...

first_num = 0
second_num = 1

for numbers in range(11):
    print(first_num)
    first_num, second_num = second_num, first_num+second_num