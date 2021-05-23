# Zadej rozměry šachovnice
size = 10
# Zadej symboly
symbols = " ","#"


# Vytvoř šachovnici
rady = list(range(1, 11))


# Doplň smyčky for, které by měly postupně nahrát celou
# šachovnici do proměnné 'desk'

# Vytiskni šachovnici.

"""
def desk():
    cs = 1
    while cs <= size:
        cs += 1
        if cs % 2 == 1:
            for pole in rady:
                if pole % 2 == 0:
                    print(symbols[0],end="")
                else:
                    print(symbols[1],end="")

            print()
        else:
            for pole in rady:
                if pole % 2 == 0:
                    print(symbols[1], end="")
                else:
                    print(symbols[0], end="")

            print()



desk()

"""
