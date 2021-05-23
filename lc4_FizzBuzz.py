#Napiš program, který tiskne celá čísla od 1 do 100 (včetně).
#Ale:
#pro násobky 3 vytiskni Fizz (namísto čísla)
#pro násobky 5 vytiskni Buzz (namísto čísla)
#pro násobky 3 a 5 zároveň vytiskni FizzBuzz (namísto čísla)

cisla = list(range(1,101))
for cs in cisla:
    if (cs % 3 == 0) and (cs % 5 == 0):
        print("FizzBuzz")
    elif cs % 3 == 0:
        print("Fizz")
    elif cs % 5 ==0:
        print("Buzz")
    else:
        print(cs)
