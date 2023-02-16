# Lê uma lista de tamanho n e imprime duas, uma impar, outra par mais ela mesmo
n=int(input("Digite o tamanho da lista:"))
while n<0:
    n=int(input("Inválido, digite outro tamanho:"))

v1=[0]*n
v_impar=[]
v_par=[]
for i in range(n):
    v1[i]=int(input("Digite um número:"))
    
for i in range(n):
    if v1[i]%2 ==0:
        v_par=v_par+[v1[i]] # Ao somar uma lista com outra ele a extende
    else:    
        v_impar=v_impar+[v1[i]]


print("A lista digitada é --> %s " %v1)
print("A lista número impar --> %s " %v_impar)
print("A lista número par --> %s " %v_par)



# Solução do professor

# Ficar sempre extendendo a lista é custoso para a memória, logo é melhor definir o tamanho mesmo que seja totalmente utilizado
# usar:
# par=par[:qp]
# imp=imp[:qi]
# para retirar os números 0 indesejados 
# a solução é parecida que a acima, mas indexando com o índice das listas e utilizando um contador para os pares e ímpares cada