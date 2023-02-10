# Exercício 15 

print("Escolha o intervalo de números para descobrir quais são primos ")
inicio=input("Digite o começo do intervalo: ")
final=input("Digite o final do intervalo: ")
inicio=int(inicio)
final=int(final)+1
for numero in range(inicio, final, 1):
    texto=""
    for divisor in range(2, final, 1):
        # print("O divisor é: ", divisor)   
        if numero>1 and numero > divisor : 
            # print("Dividindo {}/{} e pegando o resto da divisão".format(numero,divisor))
            resto = numero%divisor
            if resto ==0:
                texto="nao é primo"
                # print("O número :", numero, " Não é primo")
            if texto=="nao é primo": # Basta apenas um número ser capaz de dividir o numerador, essa condição faz com que ele pare de dividir no primeiro número que for capaz de dividir o numerador.
                break
    if texto != "nao é primo" and numero>1:
        print('numero', numero, 'é primo')         
    else:
        pass
