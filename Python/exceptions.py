try:
    num = 5/2
    f1 = open("moshe")
except FileNotFoundError:
    print('No such file')
except ZeroDivisionError:
    print('do not divide by zero')