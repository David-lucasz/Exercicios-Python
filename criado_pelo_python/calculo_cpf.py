cpf_original = input("digite o seu cpf apenas numeros: ")
i = 0
cpf_9 = ""
while i < 9:                     # enquanto i for menos q 9 
    cpf_9+=cpf_original[i]
    i+=1
print(cpf_9)
peso = 10
resultado = 0
i = 0
while i < 9:
    resultado+=int(cpf_9[i]) * peso
    peso-=1
    i+=1
print(resultado)
resto = resultado % 11
if resto < 2:
        cpf_9 += "0"
else:
        cpf_original += str(11-resto)

print(cpf_9)