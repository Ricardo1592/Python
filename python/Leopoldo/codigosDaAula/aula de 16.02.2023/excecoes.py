# import sys 
# test = [1,2,3]
# qtde_sucessos_operacao = 15
# qtde_falhas_operacao = 0
# try:
#     print('antes do primeiro erro')
#     print(qtde_sucessos_operacao/qtde_falhas_operacao)
#     print('antes do segundo erro')
#     print(test[3])
#     print('antes do terceiro erro')
#     # print(test[3])
#     print('após todos os erros em potencial')
# except (IndexError, ZeroDivisionError):
#     print('algum erro aconteceu')
# # except ZeroDivisionError as e:
# #     print(e.args)
# #     print("tentou dividir por zero")
# except:
#     print( sys.exc_info())
#     print("tentou acessar índice inexistente")



try:
    print('entrei no primeiro bloco try')
    try:
        print('entrei no segundo bloco try')
        1/0
        int('abc')
        print('saindo do segundo bloco try')
    except IndexError as var_excecao:

        print('houve algum erro de acesso a índice de listas/string')
    print('saindo do primeiro bloco try')
except ZeroDivisionError as var_excecao:
    print(type(var_excecao))
    print(var_excecao)
    print('capturei um erro de divisão por zero')
except:
    print('houve algum outro erro...')
else:
    print('não houve nenhum erro lançado')
finally:
    print('independente se houve algum erro, executa aqui')
