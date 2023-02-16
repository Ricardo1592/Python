# cada linha representa uma modalidade, e vai ser colocada como linha da matriz, ou seja uma lista dentro de outra lista

mn=input()
paises=int(mn.split()[0])
modalidades=int(mn.split()[1])
ouro=0
prata=0
bronze=0
linhas=[]
paisesId={}
medalhas=[]
for i in range(modalidades):
    modalidade=input()
    mod=modalidade.split()
    print(mod)
    linhas.append([int(i) for i in mod])

j=0
print(linhas)
for mod in linhas:
    for pais in range(1,paises+1):
        if pais in mod:
            medalha=mod.index(pais)
            paisesId[pais]=[medalha]    

print(paisesId)
    