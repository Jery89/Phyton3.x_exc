def fibo_func(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fibo_func(number - 1) + fibo_func(number - 2)

print(fibo_func(8))
