names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

for i in range(len(names)):
    for y in range(len(names)):
        if names[i] < names[y]:
            names[i], names[y] = names[y], names[i]


sorted_names = list(names)

print(sorted_names)