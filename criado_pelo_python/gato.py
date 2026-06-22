class gato:
    
    def __init__(self,raca:str,cor:str,tipo_pelo:str,idade:int,nome: str):
        """
        Docstring for __init__
        
        :param self: comando que faz os atrubutos e metodos olharem para classe
        :param raca: digite a raça do gato
        :type raca: str
        :param cor: a cor do gato
        :type cor: str
        :param tipo_pelo: digite o tipo do do gato(sem pelo, pelo longo, pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato (so numeros inteiros)
        :type idade: int
        :param nome: digite a idade do gato
        :type nome: str
        """
        self.nome = nome
        self.idade = idade
        self.tipo_pelo = tipo_pelo
        self.raca = raca
        self.cor = cor
        
        def miar(self):
            print(f"o {self.nome} miou")

        meu_gato = gato("angora", "branco", "sem pelo", 17, "pedro")
        meu_gato.miar()




