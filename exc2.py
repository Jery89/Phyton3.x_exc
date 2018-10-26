number = input('please tap a number')
some_number = 10
if number == some_number:
    print('the numbers are equal!')
else:
    print('number are not equal')

some_number = raw_input('please give me another number')

if some_number == number:
    print('numbers are equal')
elif some_number % number == 0 or number % some_number == 0:
    print('the number can be devided w/o the rest')
