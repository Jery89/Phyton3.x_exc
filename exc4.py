#exc3

bufor = int(raw_input("Please input number: "))

for x in range(1, bufor):
    if bufor % x == 0:
        print(" divisor of number %s is %s " % (bufor, x))

