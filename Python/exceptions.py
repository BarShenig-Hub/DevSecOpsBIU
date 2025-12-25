
def do_math(b):
    num = 10 / b
    return num
    
def provide_nums():
    for num in range(-5, 6):
        b = num
        print('b =', b)
        try:
            result = do_math(b)
            print('result of division is', result)
        except Exception as e:
            print(type(e))
            print(e)
            print('b is', b, 'and therefore it\'s led to an exception')


def main():
    provide_nums()

main()