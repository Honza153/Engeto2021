sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
lst_sent = list(sentence)
delka = len(lst_sent)
int(delka)

sou = ["a", "e", "i", "o", "u","y"]
samo = ["h", "c","h", "k", "r", "d", "t", "n","b", "f", "l", "m", "p", "s", "v", "z","g","w"]
pct_sou = 0
pct_samo = 0

for i in range(0,delka):
    if lst_sent[i].lower() in sou:
        pct_sou += 1
    elif lst_sent[i] in samo:
        pct_samo += 1
    else:
        continue
pocet = {"No. consonants": pct_samo, "No. vowels": pct_sou}
print(pocet)

