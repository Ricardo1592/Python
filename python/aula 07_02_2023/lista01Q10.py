# Ler o número digitado N e depois ler N números inteiros e os transforma em algarismo romano até no máximo 4000 
n= input('Digite um número:')
i=1
while i<=int(n):
    casas=str(i)
    nCasas=len(casas)
    if nCasas > 3: n4=int(casas[-4])
    if nCasas > 2: n3=int(casas[-3])
    n1=int(casas[-1])
    if n1==1:
        romano1="I"
    if n1==2:
        romano1="II"    
    if n1==3:
        romano1="III"
    if n1 ==4:
        romano1="IV"
    if n1 ==5:
        romano1="V"
    if n1==6:
        romano1="VI"
    if n1==7:
        romano1="VII"    
    if n1==8:
        romano1="VIII" 
    if n1 ==9:
        romano1="IX"
    if n1 ==0:
        romano1=""        
    if nCasas==1: print("O número ", i, " em romano é -->", romano1)

    if nCasas > 1: 
        n2=int(casas[-2])
        if n2==1:
            romano2="X" + romano1
        if n2==2:
            romano2="XX" + romano1    
        if n2==3:
            romano2="XXX" + romano1
        if n2 ==4:
            romano2="XL" + romano1
        if n2 ==5:
            romano2="L" + romano1
        if n2==6:
            romano2="LX" + romano1
        if n2==7:
            romano2="LXX" + romano1    
        if n2==8:
            romano2="LXXX" + romano1 
        if n2 ==9:
            romano2="XC" + romano1
        if n2 ==0:
            romano2=romano1  
        if nCasas==2: print("O número ", i, " em romano é -->", romano2)   
    
    if nCasas > 2: 
        n3=int(casas[-3])
        if n3==1:
            romano3="C" + romano2
        if n3==2:
            romano3="CC" + romano2    
        if n3==3:
            romano3="CCC" + romano2
        if n3 ==4:
            romano3="CD" + romano2
        if n3 ==5:
            romano3="D" + romano2
        if n3==6:
            romano3="DC" + romano2
        if n3==7:
            romano3="DCC" + romano2    
        if n3==8:
            romano3="DCCC" + romano2 
        if n3 ==9:
            romano3="CM" + romano2
        if n3 ==0:
            romano3=romano2    
        if nCasas==3:print("O número ", i, " em romano é -->", romano3)        
    
    if nCasas > 3 and i<4000: 
        n4=int(casas[-4])
        if n4==1:
            romano4="M" + romano3
        if n4==2:
            romano4="MM" + romano3    
        if n4==3:
            romano4="MMM" + romano3
        print("O número ", i, " em romano é -->", romano4)

    i=i+1