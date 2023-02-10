# Lê uma lista de tamanho n e imprime duas, uma impar, outra par mais ela mesmo
n=int(input("Digite o tamanho da lista:"))
v1=[0]*n
v_impar=[]
v_par=[]
for i in range(n):
    v1[i]=int(input("Digite um número:"))
    
for i in range(n):
    if v1[i]%2 ==0:
        v_par=v_par+[v1[i]]
    else:    
        v_impar=v_impar+[v1[i]]


print("A lista digitada é --> %s " %v1)
print("A lista número impar --> %s " %v_impar)
print("A lista número par --> %s " %v_par)

