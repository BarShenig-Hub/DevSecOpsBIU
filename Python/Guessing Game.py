number_gussed = int(input("Choose a random number between 1 to 100: "))

number_checked = 50
half_the_diffrance = 50
user_input = ''

if number_gussed < 0 or number_gussed > 100:
    print("Incorrect Value!")
    exit()

while number_checked != number_gussed:
    user_input = input("Is it greater or equal to than "+str(number_checked)+"?")
    half_the_diffrance = half_the_diffrance // 2
    if half_the_diffrance < 1:
        half_the_diffrance = 1
    if user_input == 'n':
        number_checked -= half_the_diffrance
    elif user_input == 'y':
        number_checked += half_the_diffrance
    


print("It is ", number_gussed, "!!!!")