num=int(input("Digite um número até 5 dígitos: "))
lista=[]
while num<0 or len(str(num)) >5:
    num=int(input("Inválido. Digite um número até 5 dígitos: "))

def qtd_noves(num,n=9):
    num=str(num)
    qtd=0
    lista=[]
    for num2 in num:
        numero=int(num2)
        lista=lista+[numero]
        if numero == n:
            qtd=qtd+1
    return qtd, lista 

def qtd_numero(num,n):
    num=str(num)
    qtd,lista=qtd_noves(num,n)
    i=0
    qtd=0
    while lista[i]==0:
        del list[i]    
    for numero in lista:
        lista=lista+[numero]
        if numero == n:
            qtd=qtd+1
    return qtd
n=int(input("Digite um algarismo a ser procurado: "))
while n<0 or len(str(n))>1:
    n=int(input("Inválido. Digite um número entre 0 e 9: "))
print(qtd_numero(num,n))
# qtd,lista=qtd_noves(num)

# Solução do professor, para armazenar os dígitos na lista

# def separa(n) 
#     lis=[]
#     while n >0:
#         lis.insert(0, n%10)  # Para pegar os dígitos sem transformar em string, podemos dividir por 10 e pegar o resto
#         n= n //10
#     return lis     