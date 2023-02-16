import sys
def soma_digitos(s):
   for d in s:
        try:
            soma=soma+int(d)
        except ValueError:
            continue
        
    return soma

print(soma_digitos('abc'))