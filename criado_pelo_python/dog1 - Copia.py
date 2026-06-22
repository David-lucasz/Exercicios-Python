class Dog:                                         #class dog serve para criar outros cachorros
    def __init__(self, name , age):
        self.name = name                            # self se refere a propia classe eu cachorro rolei   quando coloca self ele olha para si
        self.age = age                              # cachorro caga come corre isso sao funçoes             # name,age sao passagens  passa o nome e a idade para o cao

                                                    # cachoro tem quatro patas orelhas boca rabo isso é a caracteristicas

    def sit(self):                                   
        print(F"O {self.name} sentou ")             # o cachorro sentou isso e uma funçao

    def roll_over(self):
        print(f"o {self.name} rolou")                #funçao

meu_cachorro = Dog ("pedro",17)
meu_cachorro.sit()
meu_cachorro.roll_over()