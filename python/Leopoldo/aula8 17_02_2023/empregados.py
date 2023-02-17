
Class Empregado:
    def __init__(self, id, nome, endereco='', cidade='', salario=0, bonus=0):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.salario = salario
        self.salario = salario

    def valor_salario(self):
        return self.salario + self.bonus

if name == __main__:
    print(type(Empregado))    
    print(type(Empregado.valor_salario))    