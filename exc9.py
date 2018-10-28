import random as rm

while True:
    ran_number = rm.randrange(1, 9)
    bufor = int(raw_input('guess what number was chose form 1-9?: '))
    if ran_number == bufor:
        print('great, you chosed right number')
    else:
        print('numbers are not the same, ran number is %i' % ran_number)

