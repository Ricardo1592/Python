class Pilha:
    #ultimo elemento a entrar, é o primeiro a sair (LIFO)
    def __init__(self, tamanho):
        if tamanho > 0: 
            self.__tamanho = tamanho
            self.__total = 0
            self.__elementos = []
        else:
            raise ValueError('Tamanho da pilha deve ser um número inteiro positivo.')
    #insere o elemento no topo da pilha, caso ainda haja espaço
    def push(self, elemento):
        if self.__total < self.__tamanho:
            self.__elementos.append(elemento)
            self.__total += 1
            # self.__total = len(self.__elementos)
        else:
            raise StackOverflow()
    #remove o elemento que está no topo da pilha e retorna
    def pop(self):
        if self.__total>0:
            self.__total-=1
            return self.__elementos.pop()
        raise StackUnderflow()
    #retorna o elemento atualmente no topo, sem removê-lo
    def peek(self):
        if self.__total>0:
            return self.__elementos[-1]
        raise StackUnderflow()
    #retorna True ou False, dependendo do estado da pilha
    def isEmpty(self):
        return self.__total == 0 
    #retorna a quantidade de elementos na pilha (int)
    def size(self):
        return self.__total

class StackOverflow(Exception):
    pass

class StackUnderflow(Exception):
    pass

if __name__=='__main__':
    # p2 = Pilha(-2)
    p = Pilha(2)
    print(p.size())
    print(p.isEmpty())
    # print(p.pop())
    p.push('primeiro elemento')
    # print(p.pop())
    p.push('segundo elemento')
    print(p.pop())
    p.push('terceiro elemento')
    print(p.pop())
    