def desconto(preco=0.0, taxa=0.0):
    """a funcao desconto calcula o valor de desconto de um determinado preço"""   
    #esse comentario serve para documentar a funçao
    valor_desconto = preco * (taxa / 100)
    return preco - valor_desconto


rs = desconto(100,4.2)

print(f"o valor do desconto e {rs}")







                                                              