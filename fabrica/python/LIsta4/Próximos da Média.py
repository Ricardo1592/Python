import math
n=int(input())
numbers=[]
for i in range(n):
    num=float(input())
    numbers=numbers+[num]

numbers.sort()
soma=sum(numbers)
media=soma/len(numbers)
diferença=media-numbers[0]
numero=numbers[0]
for number in numbers:
    if math.fabs(media-number) < diferença:
        diferença=math.fabs(media-number)
        numero=number

print('MEDIA: {:.2f}'.format(media))
print('MAIS PROXIMO: {:.2f}'.format(numero))
print('DIFERENCA: {:.2f}'.format(diferença))
   
