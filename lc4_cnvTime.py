# Získej vstup uživatele do proměnné `time`
cas = input("Zadej čas ve formátu[HH:MM]: ")

# Rozděl do listu vstup od uživatele do proměnné `hours` a `mins`.
lst = [cas[0:2],cas[3:5]]
hours = int(lst[0])
min = int(lst[1])
mins = lst[1]
daytime = ("AM","PM")

# Uprav proměnou `hours` tak, aby se do proměnné `adjusted_hours` místo
# 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).

# Do proměnné `daytime` vyber odpovídající string z dvojčlenného listu ['AM', 'PM']

# Vytiskni převedený čas.

if hours in range(0,24) and min in range(0,60):
   if hours in range(0,13):
        lst.clear()
        lst.insert(0,hours)
        lst.insert(1, mins)
        lst.insert(2,daytime[0])
        print("Converted to English format: ",lst[0],":",lst[1]," ",lst[2])
   else:
        adjusted_hours = hours - 12
        lst.insert(0,adjusted_hours)
        lst.insert(1, mins)
        lst.insert(2,daytime[1])
        print("Converted to English format: ",lst[0],":",lst[1]," ",lst[2])
else:
    print("Neplatný časový rozvrh")
    exit(-1)











