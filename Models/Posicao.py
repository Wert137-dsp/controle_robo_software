class Posicao():
    
    def __init__(self):
        self.__lista_movimento = {}
        self.nome = ""
        

    def posicao(self, nome, eixo1 = 0, eixo2 = 0, eixo3 = 0, eixo4 = 0, eixo5 = 0, eixo6= 0):
        
        self.__lista_movimento["Nome"] = nome
        self.__lista_movimento["Eixo1"] = eixo1
        self.__lista_movimento["Eixo2"] = eixo2
        self.__lista_movimento["Eixo3"] = eixo3
        self.__lista_movimento["Eixo4"] = eixo4
        self.__lista_movimento["Eixo5"] = eixo5
        self.__lista_movimento["Eixo6"] = eixo6

    def get_lista_movimento(self):
        return self.__lista_movimento
        