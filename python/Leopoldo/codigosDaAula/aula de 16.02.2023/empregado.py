class Empregado(object):
    def __init__(self, id, nome, endereco, cidade, salario=0, bonus=0):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.salario = salario
        self.bonus = bonus
    
    def valor_salario(self):
        return self.salario+self.bonus
        
if __name__ == '__main__':
    e = Empregado('123','Leopoldo','Rua tal', 'Recife', 1200, 300)
    e2 = Empregado('456','Teste','Rua tal', 'Recife', 100, 300)
    print(e)
    print(e.nome)
    e.nome = 'Leopoldo Teixeira'
    print(e.nome)
    print('salário total', str(e.valor_salario()))
    print('salário total', str(e2.valor_salario()))
    
    
    
    