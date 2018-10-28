while True:
    bufor = int(raw_input('Please insert some numebr: '))
    l_pierwsza = [1, bufor]
    podzielniki = [x for x in range(1, bufor+1) if bufor % x == 0]
    if podzielniki == l_pierwsza:
        print('liczba %i jest liczba pierwsza' % bufor)
        print('podzielniki:')+str(podzielniki)
    else:
        print('liczba %i nie jest liczba pierwsza' % bufor)
        print('podzielniki:') + str(podzielniki)
#znajdowanie liczb pierwszych