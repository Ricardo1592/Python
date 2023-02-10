data=input()
dia, mes, ano= map(int, data.split())
bissexto=0
if ano%100==0 and ano%400==0:
    bissexto= ano
    
if ano%4 == 0 and ano%100!=0:
    bissexto= ano
if mes>0 and dia>0 and ano>0:
    if mes < 8 and mes!=2 and mes%2!=0 and dia<=31:
        print('valida')   
    elif mes >= 8 and mes%2==0 and dia<=31:
        print('valida')
    elif mes==2 and bissexto==ano and dia<=29:    
        print('valida')
    elif mes==2 and bissexto!=ano and dia<=28:    
        print('valida')    
    else:
        print('invalida')  
else:
    print('invalida')           