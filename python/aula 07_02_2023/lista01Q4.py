# Soma todos os números pares entre 50 e 100
soma=0
for i in range(50, 101):
    resto= i%2
    if resto==0:
        soma= soma + i
print("A soma dos numeros pares entre 50 e 100 é:", soma)        