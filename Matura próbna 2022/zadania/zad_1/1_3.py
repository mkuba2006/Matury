tablica = []

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
    
    
    
    
    
before=False
Now=False 

ileb = 0   
ilec = 0  
  
for t in tablica:
    czy_bialy=False
    czy_czarny=False
    
    col1 = ''
    col2 = ''
    col3 = ''
    col4 = ''
    col5 = ''
    col6 = ''
    col7 = ''
    col8 = ''
    
    for r in t:
        col1 +=r[0]
        col2 +=r[1]
        col3 +=r[2]
        col4 +=r[3]
        col5 +=r[4]
        col6 +=r[5]
        col7 +=r[6]
        col8 +=r[7]
        
        nr =r.replace('.', '')
        czy_w_przed_lub_po_K = 'w' in nr and ('K' in nr[nr.index('w') - 1] if nr.index('w') > 0 else False or 'K' in nr[nr.index('w') + 1:] if nr.index('w') < len(nr) - 1 else False)
        czy_W_przed_lub_po_k = 'W' in nr and ('k' in nr[nr.index('W') - 1] if nr.index('W') > 0 else False or 'k' in nr[nr.index('W') + 1:] if nr.index('W') < len(nr) - 1 else False)
        if czy_w_przed_lub_po_K:
            czy_czarny=True
        if czy_W_przed_lub_po_k:
            czy_bialy=True
        
        
        
        
    cl1 = col1.replace('.', '')
    cl2 = col2.replace('.', '')
    cl3 = col3.replace('.', '')
    cl4 = col4.replace('.', '')
    cl5 = col5.replace('.', '')
    cl6 = col6.replace('.', '')
    cl7 = col7.replace('.', '')
    cl8 = col8.replace('.', '')
    q11 = 'w' in cl1 and ('K' in cl1[cl1.index('w') - 1] if cl1.index('w') > 0 else False or 'K' in cl1[cl1.index('w') + 1:] if cl1.index('w') < len(cl1) - 1 else False)
    q12 = 'W' in cl1 and ('k' in cl1[cl1.index('W') - 1] if cl1.index('W') > 0 else False or 'k' in cl1[cl1.index('W') + 1:] if cl1.index('W') < len(cl1) - 1 else False)
        
    q21 = 'w' in cl2 and ('K' in cl2[cl2.index('w') - 1] if cl2.index('w') > 0 else False or 'K' in cl2[cl2.index('w') + 1:] if cl2.index('w') < len(cl2) - 1 else False)
    q22 = 'W' in cl2 and ('k' in cl2[cl2.index('W') - 1] if cl2.index('W') > 0 else False or 'k' in cl2[cl2.index('W') + 1:] if cl2.index('W') < len(cl2) - 1 else False)        
        
    q31 = 'w' in cl3 and ('K' in cl3[cl3.index('w') - 1] if cl3.index('w') > 0 else False or 'K' in cl3[cl3.index('w') + 1:] if cl3.index('w') < len(cl3) - 1 else False)
    q32 = 'W' in cl3 and ('k' in cl3[cl3.index('W') - 1] if cl3.index('W') > 0 else False or 'k' in cl3[cl3.index('W') + 1:] if cl3.index('W') < len(cl3) - 1 else False)    
        
    q41 = 'w' in cl4 and ('K' in cl4[cl4.index('w') - 1] if cl4.index('w') > 0 else False or 'K' in cl4[cl4.index('w') + 1:] if cl4.index('w') < len(cl4) - 1 else False)
    q42 = 'W' in cl4 and ('k' in cl4[cl4.index('W') - 1] if cl4.index('W') > 0 else False or 'k' in cl4[cl4.index('W') + 1:] if cl4.index('W') < len(cl4) - 1 else False)    
        
    q51 = 'w' in cl5 and ('K' in cl5[cl5.index('w') - 1] if cl5.index('w') > 0 else False or 'K' in cl5[cl5.index('w') + 1:] if cl5.index('w') < len(cl5) - 1 else False)
    q52 = 'W' in cl5 and ('k' in cl5[cl5.index('W') - 1] if cl5.index('W') > 0 else False or 'k' in cl5[cl5.index('W') + 1:] if cl5.index('W') < len(cl5) - 1 else False)
    
    q61 = 'w' in cl6 and ('K' in cl6[cl6.index('w') - 1] if cl6.index('w') > 0 else False or 'K' in cl6[cl6.index('w') + 1:] if cl6.index('w') < len(cl6) - 1 else False)
    q62 = 'W' in cl6 and ('k' in cl6[cl6.index('W') - 1] if cl6.index('W') > 0 else False or 'k' in cl6[cl6.index('W') + 1:] if cl6.index('W') < len(cl6) - 1 else False)
    
    q71 = 'w' in cl7 and ('K' in cl7[cl7.index('w') - 1] if cl7.index('w') > 0 else False or 'K' in cl7[cl7.index('w') + 1:] if cl7.index('w') < len(cl7) - 1 else False)
    q72 = 'W' in cl7 and ('k' in cl7[cl7.index('W') - 1] if cl7.index('W') > 0 else False or 'k' in cl7[cl7.index('W') + 1:] if cl7.index('W') < len(cl7) - 1 else False)
    
    q81 = 'w' in cl8 and ('K' in cl8[cl8.index('w') - 1] if cl8.index('w') > 0 else False or 'K' in cl8[cl8.index('w') + 1:] if cl8.index('w') < len(cl8) - 1 else False)
    q82 = 'W' in cl8 and ('k' in cl8[cl8.index('W') - 1] if cl8.index('W') > 0 else False or 'k' in cl8[cl8.index('W') + 1:] if cl8.index('W') < len(cl8) - 1 else False)
    if q11 or q21 or q31 or q41 or q51 or q61 or q71 or q81 :
        czy_czarny=True    
    if q12 or q22 or q32 or q42 or q52 or q62 or q72 or q82 :
        czy_bialy=True
    
    
    
    if before == False:   
        if czy_bialy ==True:
            ileb+=1
            
        if czy_czarny ==True:
            ilec+=1
            
        before=True
    else:
        before=False
        
    print(czy_bialy,czy_czarny)
    
    
    
print(ileb/2)
print(ilec/2)    
        
    

        
    