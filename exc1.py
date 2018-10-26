name = raw_input('What is your name?: ')
age = raw_input('Please give me you year of birth: ')

birth = 2018 - (2018 - int(age)) + 100

print("Hello %s you will be 100yo in %i" % (name, birth))
