# Calcula média de N alunos fornecidos e mostra quais notas são maiores que a média 
n=int(input("Digite o número de alunos:"))
notas=[0]*n
media=0
for i in range (n):
    notas[i]=float(input("Digite a nota:"))

soma=sum(notas)
media=soma/n
for i in range (n):
    if notas[i] > media:
        print("A nota %.2f é maior que a média %.2f " %(notas[i], media) )

    
    

