class Toy:
    def __init__(self, L = []):
        self._elems = L
    def add(self, new_e):
        self._elems.append(new_e)
    def size(self):
        return len(self._elems)
    # def __init__(objeto):
    #     objeto._elems = []
    # def add(objeto, new_e):
    #     objeto._elems.append(new_e)
    # def size(objeto):
    #     return len(objeto._elems)


if __name__ == '__main__':
    x = [1,2,3]
    t1 = Toy()
    t2 = Toy()
    t3 = Toy.__new__(Toy)
    Toy.__init__(t3,[1,2,3])
    print(t3._elems)
    # Toy.add(x,4)
    Toy.add(t1,4)
    t1.add(4)
    print(t1.size())
    print(Toy.size(t1))
    print(t1)