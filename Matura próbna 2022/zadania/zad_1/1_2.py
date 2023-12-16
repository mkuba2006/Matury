
tablica = []

with open('C:/Users/mkuba/OneDrive/Pulpit/Matury/Matura próbna 2022/dane/szachy.txt') as file:
    ruchy = []
    
    for line in file:
        line = line.strip()
        if line:
            tab=[]
            ruchy.append(line)
            tab.append(line)
        else:
            tablica.append(ruchy)
            ruchy = []

        
        


if ruchy:
    tablica.append(ruchy)

lacznie=0
najmniej=100
dummy=0
for t in tablica:
    białe = 0
    czarne = 0
    
    
    K=0
    W=0
    S=0
    H=0
    G=0
    P=0
    
    k=0
    w=0
    s=0
    h=0
    g=0
    p=0
    
    
    
    
    for l in t:
        
        for x in l:
            if x == '.':
                dummy+=1
                
            else:
                if x.isupper():
                    białe += 1
                    if x == 'K':
                        K+=1
                    if x == 'W':
                        W+=1
                    if x == 'S':
                        S+=1
                    if x == 'H':
                        H+=1
                    if x == 'G':
                        G+=1
                    if x == 'P':
                        P+=1    
                else:
                    czarne += 1
                    if x == 'k':
                        k+=1
                    if x == 'w':
                        w+=1
                    if x == 's':
                        s+=1
                    if x == 'h':
                        h+=1
                    if x == 'g':
                        g+=1
                    if x == 'p':
                        p+=1    
              
              
              
                
    if białe == czarne and K==k and W==w and S==s and H==h and G==g and P==p:
        lacznie+=1
        print(t)
        print("białe:", białe)
        print("czarne:", czarne)
        print('suma:', K+k+W+w+S+s+H+h+G+g+P+p)
        print("\n")
        
        if K+k+W+w+S+s+H+h+G+g+P+p < najmniej:
            najmniej=K+k+W+w+S+s+H+h+G+g+P+p
    
print(lacznie)
print(najmniej)
