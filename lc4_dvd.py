start = input("Zadej počáteční číslo: ")
stop = input("Zadej poslední číslo: ")
divisor = input("Zadej dělitele: ")

lst_cs = list(range(int(start),int(stop)+1))
lst_delence = list()
print(lst_cs)

for i in range(0,len(lst_cs)):
    if int(lst_cs[i] ) % int(divisor) == 0:
        lst_delence.append(lst_cs[i])
    else:
        continue

print("Numbers in range: ",start,stop," divisible by ",divisor,"\n",lst_delence)

