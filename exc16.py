import random as ram

def password_gen():
    out = []
    tab = 'ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz1234567890'
    for x in range(8):
        out.append(tab[ram.randint(0, 57)])
    return "".join(out)
print(password_gen())