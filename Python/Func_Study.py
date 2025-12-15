def myFunc():
    print("myFunc !!!!")

f2 = myFunc

print(f"f2 calls: {f2}")
print(f"myFunc calls: {myFunc}")

print(f"ID of f2: {id(f2)}")
print(f"ID of myFunc: {id(myFunc)}")


def sub_num(a, b): # parameters
    print(a+b)

sub_num(3, 5) # arguments

# positional arguments follows keyword arguments

sub_num (3, b=10)

def add_nums(x, y=5): # default value y = 5
    print(x+y)

add_nums(3, 4)
add_nums(3)

def add_numbers(a, b, c, *, d, e): # from the asterisk must be keywords
    print(a+b+c+d+e)

add_numbers(5,6,7,e=8, d=9)

def add_numbers(a, b, c, /, d, e): # before the slash must be positional
    print(a+b+c+d+e)

add_numbers(5,6,7,e=8, d=9)

def add_numbers(a, b, *others): # others = tuples
    print(type(others))
    print(others) # packing to tuple

add_numbers(1, 2, 3, 4)

def show_all(*all):
    for x in all:
        print(x, end= ' ')

show_all(1, 2, 3, 4, 5, 6, 7)
print()

lst = []
def sum_all(*all):
    for num in all:
        lst.append(num)
    print(f"Sum all numbers: {sum(lst)}")

sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9)
        

