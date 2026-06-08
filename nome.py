#amos usar  uma variavel chamada nome para
#gurdar o nome do cliente. utilizaremos tambem 
#o comando input (-> dentro | put-> por em algum lugar)
nome = input("digite seu nome: ")
print ("ola, " +nome+ "! bem-vindo ao python!")

# o operador +(mais) foi ultilizade para 
#juntar o texto o texto entre aspas("")
#com a variavel nome
print(f"ola, sr(a). {nome}")

#abaixo usamos o comando print com a letra f (format)
#para inserir uma variavel no meio de uma string.
#a variavel foi inserida com chaves  ({})
#esta tecnica e chamada de interpolaçao
print(f"ola, sr(a). {nome}. seja bem-vindo")
