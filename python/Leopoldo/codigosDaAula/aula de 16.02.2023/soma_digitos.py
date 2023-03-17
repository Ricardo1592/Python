def soma_digitos(s):
    """Assumir que s é uma string
       retornar a soma dos dígitos decimais de s
       por exemplo, se s é '123' retorna 6
       por exemplo, se s é 'abc' retorna 0
       por exemplo, se s é 'a1b2c' retorna 3
       só pode usar for, try, except, int"""
    soma = 0 
    for letra in s:
        try:
            soma = soma + int(letra)
        except ValueError:
            continue
    return soma

print(soma_digitos('123'))#6
print(soma_digitos('abc'))#0
print(soma_digitos('a1b2c'))#3
print(soma_digitos('3a4b5c'))#11