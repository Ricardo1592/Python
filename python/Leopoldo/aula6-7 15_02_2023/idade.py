from datetime import date
hoje=date.today()
print(hoje)
ano = 1992
mes = 9
dia = 15
data_nascimento= date(ano, mes, dia)
dias=hoje - data_nascimento
print(dias.days)

if isinstance(dias):
    print("Is instance")