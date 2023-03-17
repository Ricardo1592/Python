from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self,id,nome,endereco, cidade="", dataNascimento=None):
        # super().__init__(id,nome,endereco,cidade,dataNascimento)
        Pessoa.__init__(self,id,nome,endereco,cidade,dataNascimento)
        self.qtde_compras = 0
    def __str__(self):
        return f'Cliente com nome {self.nome} e CPF {self.id}'

if __name__=='__main__':
    p1 = Pessoa('123','Teste')
    p2 = Pessoa('123','Teste')
    c1 = Cliente('123','Teste','Sem endereço ainda')
    print('--esse código está rodando a partir de cliente.py--')
    # print(p1)
    # print(c1)
    # print(type(p1))
    # print(type(c1))
    print(c1.endereco)
    print('--fim do código em cliente.py--')