def fibonnacci(termo):
    if termo<=1:
        valor=termo
        return valor
    valor=fibonnacci(termo-1) + fibonnacci(termo-2)
    # print(valor)
    return valor
fibonnacci(10)

num=[]
for i in range (10):
    num.append(str(fibonnacci(i))+'\n')
print(num)   
with open('fib.txt', 'w') as arq:
    arq.writelines(num)