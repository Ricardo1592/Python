import datetime

class Pessoa(object):
    def __init__(self, id, nome, endereco="", cidade="", dataNascimento=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.dataNascimento = dataNascimento
    
    def setDataNascimento(self,data):
        self.dataNascimento = data
    
    def idadeEmDias(self):
        if self.dataNascimento == None:
            raise ValueError('Data de nascimento não definida')
        else:
            delta = datetime.date.today() - self.dataNascimento
            return (delta).days

if __name__=='__main__':
    p1 = Pessoa('123','Teste')
    # print(f'{p1.nome} tem {p1.idadeEmDias()} dias de vida hoje')
    p1.setDataNascimento(datetime.date(2023,2,15))
    p2 = Pessoa('456','Outro Teste')
    p2.setDataNascimento(datetime.date(1990,1,20))
    print(f'{p1.nome} tem {p1.idadeEmDias()} dias de vida hoje')
    print(f'{p2.nome} tem {p2.idadeEmDias()} dias de vida hoje')

    