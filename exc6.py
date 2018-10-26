bufor = raw_input('Please insert some string: ')
if bufor == ''.join(reversed(bufor)):
    print('This string is palindrome')
else:
    print('This string is not palindrome')
