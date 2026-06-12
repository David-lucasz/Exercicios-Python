#importaçao de funçoes espesificas dos modulos 
#comando from(origem) que indica de onde vem as funçoes
#ou seja de qual modulo voce esta extraindo as funçoes
# o comando import indica quais funçoes voce ira usar do (from)
#modulo carregado pelo comando from(origem)

from os import system, cpu_count                     #ctrl + espaço para ver as funçoes dentro da blibioteca( os ) 
from math import sqrt, pow, pi 


system("cls")
print("===== origem os =====")
print(cpu_count())
print("===== origem math =====")
print(sqrt(49))
print(pow(2,5))