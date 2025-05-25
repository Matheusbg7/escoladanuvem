ano = int(input("Digitee um ano: "))

if ano % 4 == 0: # Se o ano for divisivel por 4, poderá ser bissexto
    if ano % 100 == 0: # Se for divisivel por 100, tambem precisa ser verificado
        if ano % 400 == 0: # Se tambem for divisivel por 400, é bissexto
            print(f"{ano} é um ano bissexto")
        else: 
            print(f"{ano} não é um ano bissexto")
    else:
        print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")