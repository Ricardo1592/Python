class TypedAttribute:
    def __init__(self,nome,tipo,padrao=None):
        self.nome = "_" + str(nome)
        self.tipo = tipo
        self.valorPadrao = padrao if padrao!=None else type(tipo)
    def __get__(self,instance,cls):
        return getattr(instance,self.nome,self.valorPadrao)
    def __set__(self,instance,valor):
        if not isinstance(valor,self.tipo):
            raise TypeError(f'Deveria ser um valor do tipo {self.tipo}')
        setattr(instance,self.nome,valor)
    def __delete__(self,instance):
        raise AttributeError('Não pode deletar este atributo')
    
class ContaBancaria:
    nome = TypedAttribute('nome', str)
    saldo = TypedAttribute('saldo', float, 50.0)
    teste = TypedAttribute('teste', bool, False)
    qualquerTipo = 'teste'

if __name__=='__main__':
    c = ContaBancaria()
    c.nome = 'Leopoldo'
    c.saldo = 60.0
    print(c.teste)
    # print(c.nome)
    # print(c.saldo)
    # print(c.qualquerTipo)
    c.nome = 'Outro nome'
    c.saldo = 75.0
    c.qualquerTipo = False
    print(c.nome)
    print(c.saldo)
    print(c.qualquerTipo)
    # c.nome = 12
    c.saldo = '75.0'
    c.qualquerTipo = 12
    print(c.nome)
    print(c.saldo)
    print(c.qualquerTipo)
    









