class A(object):
    def __init__(self, arg1 = 'esse atributo é visível'):
        self.visivel = arg1
        self.__visivel__ = 'isso também é visível'
        self.__invisivel = 'isso aqui é invisível fora da definição da classe'
    
    def print_visivel(self):
        print(self.visivel)
        print(self.__visivel__)

    def print_invisivel(self):
        print(self.__invisivel)

class B(A):
    def teste_print_invisivel(self):
        print(self.__invisivel)

# 'A' object has no attribute '__invisivel'. 
# Did you mean: '_A__invisivel'?

if __name__=='__main__':
    a = A('alguma coisa')
    a.visivel = 'nova string'
    print(a.visivel)
    print(a.__visivel__)
    # print(a.__invisivel)
    a.print_visivel()
    a.print_invisivel()
    print('---')
    b = B()
    print(b.visivel)
    print(b.__visivel__)
    b.print_visivel()
    b.print_invisivel()
    b.teste_print_invisivel()
   


class C(B):
    pass

class D(C):
    pass

class E(D):
    pass