# Mostra em qual dia da semana 
import calendar as c

mes= c.monthcalendar(2022, 11)
if mes[0][c.THURSDAY] != 0:
    dia = mes[3][c.THURSDAY]
else:
    dia = mes[4][c.THURSDAY]

print(dia)
