seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
print(seq)
set_hod = set(seq)
lst_set = list(set_hod)
slov = {}
slov.fromkeys(lst_set)

for i in range(0,int(len(seq))):
    if seq[i] in set_hod:
        klic = seq[i]
        pocet = seq.count(klic)
        tmp = {klic: str(pocet)+"x"}
        slov.update(tmp)
    else:
        continue

print(slov)

