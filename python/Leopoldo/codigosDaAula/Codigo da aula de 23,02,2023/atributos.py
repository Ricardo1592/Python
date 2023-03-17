class A(object):
    a = 23
    b = 46
    def f(self):
        print('método f() da classe A')
    def g(self):
        print('método g() da classe A')

class B(A):
    b = 32
    c = 64
    def g(self):
        print('método g() da classe B')
        super().g()
    def h(self):
        print('método h() da classe B')

class C(B):
    def m(self):
        super().f()
        print('funcionou?')

if __name__=='__main__':
    # a1 = A()
    # a2 = A()
    # print(a1.a)
    # print(a2.a)
    # a1.a = 15
    # a1.c = 18
    # print(a1.a)
    # print(a1.c)
    # print(a2.a)
    # print(A.a)

    
    a = A()
    b = B()
    c = C()

    # a.f()
    # a.g()
    # b.f()
    # print('--- prestes a executar b.g()')
    # b.g()
    # print('--- terminou de executar b.g()')
    # c.f()
    # c.g()
    # c.h()
    # c.m()

    print(c.g)
    # print(a.f,a.g,b.f,b.g,b.h,c.f,c.g,c.h,c.m)
    