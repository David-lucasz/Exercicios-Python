def acrescimo(preco: float, taxa: float):
    """a funçao acrescimo realiza o calculo de aumento do valor do preçop do produto de acordo com a taxa 
    
args:
    preço: (float) passe o preço do produto  
    taxa:  (float) passe o taxa do acrescimo somente numeros
    
returns:
     float: retona o preço do produto com o valor  de acrescimo
    """
    return preco * (1+taxa) / 100

rs = acrescimo(2560.90, 8.9)

print(f"o valor do produto é {rs}")

