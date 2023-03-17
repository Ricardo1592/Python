from pessoa import Pessoa
from cliente import Cliente

if __name__=='__main__':
    p1 = Pessoa('123','Teste')
    c1 = Cliente('123','Teste')
    print(str(p1))
    print(str(c1))
    print(type(p1))
    print(type(c1))
    print(isinstance(p1,Pessoa))
    print(isinstance(c1,Cliente))
    print(isinstance(p1,Cliente))
    print(isinstance(c1,Pessoa))
    

