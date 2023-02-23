class Pilha:
    # Último elemento a entrar, é o último a sair (LIFO)
    def __init__(self, tamanho) -> None:
        self.pilha=[0]*tamanho
        self.tamanho=tamanho
        self.total=0
        pass
    # Insere o elemento no topo da pilha, caso ainda haja espaço
    def push(self, elemento):
        if len(self.pilha) <= self.tamanho:
            self.pilha[-1]= elemento
            self.total+=1
        return     
    # Remove o elemento que está no topo da pilha e retorna    
    def pop(self):
        if len(self.pilha) > 0:
            self.pilha= self.pilha[:-1]
            if self.total>0:
                self.total-=1 
        return    
    
    # Retorna o elemento atualmente no topo, sem removê-lo    
    def peek(self):    
        return self.pilha[-1]

    # Retorna True ou False, dependendo do estado da pilha    
    def isEmpty(self):    
        if len(self.pilha)==0: 
            return True 
        else: 
            return False
    def size (self):
        return len(self.pilha)    

if __name__=='__main__':
    p=Pilha(3)