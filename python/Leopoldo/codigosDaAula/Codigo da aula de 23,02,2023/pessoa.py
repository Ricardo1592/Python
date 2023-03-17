import datetime

class Pessoa(object):
    def __init__(self, id, nome, endereco="", cidade="", dataNascimento=None):
        self.id = id
        self.nome = nome
        try:
            self.__sobrenome = nome.split()[-1] 
        except:
            self.__sobrenome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.__dataNascimento = dataNascimento
    
    def setDataNascimento(self,data):
        if type(data) == datetime.date:
            self.__dataNascimento = data
        else: 
            raise TypeError('Data de nascimento deve ser informada como objeto do tipo datetime.date')
        
    def getDataNascimento(self):
        return self.__dataNascimento

    def getSobrenome(self):
        return self.__sobrenome

    def idadeEmDias(self):
        if self.__dataNascimento == None:
            raise ValueError('Data de nascimento não definida')
        else:
            delta = datetime.date.today() - self.__dataNascimento
            return (delta).days

if __name__=='__main__':
    p1 = Pessoa('123','Teste Sobrenome')
    # print(f'{p1.nome} tem {p1.idadeEmDias()} dias de vida hoje')
    p1.setDataNascimento(datetime.date(2023,2,15))

    p2 = Pessoa('456','Outro')
    # print(p1.getSobrenome())
    # print(p2.getSobrenome())
    p2.setDataNascimento(datetime.date(1990,1,20))
    # p1.dataNascimento = '15/2/23'
    print(f'{p1.nome} tem {p1.idadeEmDias()} dias de vida hoje')
    print(f'{p2.nome} tem {p2.idadeEmDias()} dias de vida hoje')

    