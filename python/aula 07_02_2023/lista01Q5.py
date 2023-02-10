# Calcula o fatorial de um número inteiro lido

numero=int(input('Digite o número para calcular o fatorial dele:'))
i=1
fatorial=1

while i <=numero and numero!=0:
    fatorial= fatorial*i
    i=i+1

print("O fatorial de", numero, " é:", fatorial)
