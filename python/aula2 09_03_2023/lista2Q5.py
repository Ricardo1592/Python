# Ler o nome completo do usuário e mostrar o primeiro e último de forma maiúscula

L1=int(input("Digite o tamanho do vetor 1:"))
L2=int(input("Digite o tamanho do vetor 2:"))
v1= [0]*L1
maior=L1
if L2>L1:
    maior=L2
v2= [0]*maior
vSoma=[0]*maior
for i in range(L1):
    v1[i]=input("Digite o número %d do vetor1 :" %(i+1))

for i in range(L2):
    v2[i]=input("Digite o número %d do vetor2 :" %(i+1))

print(v1)   
print(v2)   

for i in range(L2):
    vSoma[i]= int(v1[i])+int(v2[i])

print(vSoma)