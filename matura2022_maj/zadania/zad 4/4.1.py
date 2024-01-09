table = []

with open('matura2022_maj\zadania\zad 4\liczby.txt') as file:
    content = file.readlines()
    for line in content:
        liczba = line.strip()
        if(liczba[0] == liczba[-1]):
            table.append(liczba)
    
print(table[0])
print(len(table))
        
        
