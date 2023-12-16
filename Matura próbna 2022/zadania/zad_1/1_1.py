ile=0
tablica = []
najwiecej = 0

with open('C:/Users/mkuba/OneDrive/Pulpit/Matury/Matura próbna 2022/dane/szachy.txt') as file:
    ruchy = []
    
    for line in file:
        line = line.strip()
        if line:
            ruchy.append(line)
            
        else:
            tablica.append(ruchy)
            ruchy = []
    


if ruchy:
    tablica.append(ruchy)
    
for t in tablica:
    tabela1 = ''
    tabela2 = ''
    tabela3 = ''
    tabela4 = ''
    tabela5 = ''
    tabela6 = ''
    tabela7 = ''
    tabela8 = ''
    iletakich = 0
    
    for r in t:
        tak = False
        
        tabela1 += r[0]
        tabela2 += r[1]
        tabela3 += r[2]
        tabela4 += r[3]
        tabela5 += r[4]
        tabela6 += r[5]
        tabela7 += r[6]
        tabela8 += r[7]
        if tabela1 == '........':
            tak = True
            iletakich+=1

        if tabela2 == '........':
            tak = True
            iletakich+=1

        if tabela3 == '........':
            tak = True
            iletakich+=1

        if tabela4 == '........':
            tak = True
            iletakich+=1

        if tabela5 == '........':
            tak = True
            iletakich+=1

        if tabela6 == '........':
            tak = True
            iletakich+=1

        if tabela7 == '........':
            tak = True
            iletakich+=1
            
        if tabela8 == '........':
            tak = True
            iletakich+=1
            
        if tak == True:
            ile+=1
        if iletakich > najwiecej:
            najwiecej = iletakich
print(ile)
print(najwiecej)

        