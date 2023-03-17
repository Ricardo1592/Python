# while True: 
#     val = input('Digite um inteiro ou a palavra "fim" para sair: ')
#     try:
#         numero = int(val)
#         print('O número que você digitou ao quadrado é', numero**2)
#     except ValueError:
#         if val == 'fim':
#             break
#         else: 
#             print(val, "não é um número inteiro")

def read_int(): 
    return read_val(int, 'Digite um inteiro: ', 'não é um número inteiro')

def read_val(tipo, msg_digite, msg_erro):
    while True: 
        val = input(msg_digite)
        try:
            return(tipo(val))
        except ValueError:
            print(val, msg_erro)

x = read_int()
print('O número que você digitou ao quadrado é', x**2)
