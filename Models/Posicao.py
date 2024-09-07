class Posicao:
    
    def __init__(self):
        self.lista_movimento = {}

    def posicao(self, eixo1 = 0, eixo2 = 0, eixo3 = 0, eixo4 = 0):
        self.eixo1 = eixo1
        self.eixo2 = eixo2
        self.eixo3 = eixo3
        self.eixo4 = eixo4
       
        self.lista_movimento["Eixo1"] = self.eixo1
        self.lista_movimento["Eixo2"] = self.eixo2
        self.lista_movimento["Eixo3"] = self.eixo3
        self.lista_movimento["Eixo4"] = self.eixo4

        