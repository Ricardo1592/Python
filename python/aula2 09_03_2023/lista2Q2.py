# Imprimir o nome fornecido pelo usuário em escala

nome=input("Digite o seu nome:")
i=1
for letra in nome:
    print(nome[:i])
    i=i+1

# Solução do professor
for i in range (len(nome)):
    print(nome[:i+1])   