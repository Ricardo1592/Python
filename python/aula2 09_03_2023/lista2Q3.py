# Imprimir o nome fornecido pelo usuário em escala

s1=input("Digite a primeira string:")
s2=input("Digite a segunda string:")

# repet= s2.count(s1)
# print(repet)

# Sem o método count

i=0
j=len(s1)

vezes=0
for comp in s2:
    letras=s2[i:j]
    # print(letras)
    if s1==letras:
        vezes=vezes+1    
    i=i+1
    j=j+1
print(vezes)

# Solução professor

cont=0
pos=s2.find(s1) # o find retorna -1 ao não achar a string


while pos != -1
    cont=cont+1
    pos=s2.find(s1, pos+1)
print(cont)    