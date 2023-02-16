plano=input()
pagamento=input()

plano=plano.lower()
pagamento=pagamento.lower()

basico_valor= 80.80
entret_valor= 100.40
multi_valor=130.23
completo_valor= 215.50

basico_canais=32
entret_canais= 55
multi_canais=70
completo_canais= 112


if pagamento == "débito automático" and plano == "básico":
    basico_canais=basico_canais+6
    basico_valor= basico_valor - basico_valor*0.05
    print("%.2f" %(basico_valor))
    print("%d" %(basico_canais))
elif plano == "básico":
    print("%.2f" %(basico_valor))
    print("%d" %(basico_canais))


if pagamento == "débito automático" and plano == "entretenimento":
    entret_canais= entret_canais+6
    entret_valor= entret_valor - entret_valor*0.05
    print("%.2f" %(entret_valor))
    print("%d" %(entret_canais))
elif plano == "entretenimento":
    print("%.2f" %(entret_valor))
    print("%d" %(entret_canais))

if pagamento == "débito automático" and plano == "multicultural":
    multi_canais= multi_canais+11
    multi_valor= multi_valor - multi_valor*0.10

    print("%.2f" %(multi_valor))
    print("%d" %(multi_canais))
elif plano == "multicultural":
    print("%.2f" %(multi_valor))
    print("%d" %(multi_canais))

if pagamento == "débito automático" and plano == "completo":
    completo_canais= completo_canais+11
    completo_valor= completo_valor - completo_valor*0.10

    print("%.2f" %(completo_valor))
    print("%d" %(completo_canais))
elif plano == "completo":
    print("%.2f" %(completo_valor))
    print("%d" %(completo_canais))    







