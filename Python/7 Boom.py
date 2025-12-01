num = 1

while num <= 100:
    if '7' in str(num):
        print("Boom")
    if not(num % 7):
        print("Boom")
    else:
        print(num)
    num += 1

print("The game is over")
