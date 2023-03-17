class Empregado(object):
    def __init__(self, id, nome, endereco="", cidade="", salario=0, bonus=0):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.salario = salario
        self.bonus = bonus
    
    def valor_salario(self):
        return self.salario+self.bonus

if __name__ == '__main__':
    # e = Empregado('123','Leopoldo')
    # print(e.nome)
    # # print(e.dataNascimento)
    # e.dataNascimento = '28/03/1995'
    # print(e.dataNascimento)
    # e2 = Empregado('456','Teste',salario=100, bonus=300)
    # print(type(Empregado))
    # print(type(Empregado.valor_salario))
    # # print(type(m))
    # # print(type(int))
    # # print(type(2))
    # print(type(e))
    # print(type(e2))
    # print(type(e.valor_salario))
    # print(e2.valor_salario())
    # print(e2.nome)
    # e2.nome = 'Joana'
    # print(e2.nome)

    # e3 = Empregado('Id','Nome')
    # e4 = Empregado('Id','Nome')
    # print(e3.nome)
    # print(e4.nome)
    # e4.nome = 'Outro'
    # print(e3.nome)
    # print(e4.nome)

    # e5 = Empregado('Id','Nome')
    # e6 = e5
    # print(e5.nome)
    # print(e6.nome)    
    # e6.nome = 'Outro'
    # print(e5.nome)    
    # print(e6.nome)    
    
    empregados = []
    for i in range(1,5):
        empregados.append(Empregado(str(i),"Empregado #"+str(i)))
    print([e.nome for e in empregados])
    
    
    
# def m():
#     pass    