while True:
    cli = input("mycli> ")
    if not cli:
        continue
    elif cli == 'quit':
        break
    else:
        print(f'{cli} is a nice command')