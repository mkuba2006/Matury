table = []
najwiecej_czynników= []
najwieksza = []
naj2=[]
coto=[]


def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    
    return czynniki

with open('matura2022_maj/zadania/zad 4/liczby.txt') as file:
    content = file.readlines()
    for line in content:
        liczba = int(line.strip())
        najwiecej_czynników.append(rozloz(liczba))




for p in najwiecej_czynników:
    if len(p) > len(najwieksza):
        najwieksza = p
        naj2.clear()
        naj2.append(p)
    elif len(p) == len(najwieksza):
        naj2.append(p)


z=1
for x in najwieksza:
    z *= x

print('najwieksza dlugosc: ',len(najwieksza))    

for a in naj2:
    r = 1
    for b in a:
        
        r *=b
    coto.append(r)
print('najwiecej czynników: ',coto)