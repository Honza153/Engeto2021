# Zadej rozměry šachovnice
size = 10
# Zadej symboly
symbols = " #"


# Vytvoř šachovnici
pruhy = list(enumerate(symbols * 5))

# Doplň smyčky for, které by měly postupně nahrát celou
# šachovnici do proměnné 'desk'
desk = list()

cs = 0
while cs < size:
    cs += 1
    # print(cs)
    if cs % 2 == 1:
        kl = ""
        for i, j in pruhy:
            kl = kl + j

        desk.append(kl)
    else:
        lk = ""
        for i, j in reversed(pruhy):
            lk = lk + j

        desk.append(lk)

# Vytiskni šachovnici.
for i in range(0, size):
    if i % 10 != 0:
        slovo = desk[i]
        print(slovo, end="")
        print()
    else:
        print(desk[i], end="")
        print()
