palavra = "tempo"                  # defini a 
qtd_palavra = len(palavra)         # o comando len significa comprimento ou seja 
                                   # conta a quantidade de caracterer em uma coleçao
print(qtd_palavra)                 # exibe
cont = 0                           # cont = 0
while cont < qtd_palavra:          #enquando cont(0) for menor(<) que qtd_paravalavra conte mais um execute 
    print(f"A {cont+1}ª letra é {palavra[cont]}") #vai exibir a primeira letra da palavra tempo
    cont+=1