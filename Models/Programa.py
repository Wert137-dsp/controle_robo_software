class Programa():

    def __init__(self):
        self.passos = []
        self.__nome = ""
        self.__descricao = ""

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome

    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def get_descricao(self):
        return self.__descricao

    def get_programa(self):
        return self.passos
    
    def adicionar_passo(self, posicao):
        self.passos.append(posicao)
