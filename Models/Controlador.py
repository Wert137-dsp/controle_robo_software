class Robo:
    
    def __init__(self):
        self.lista_movimento = []

    def posicao(self, eixo1, eixo2, eixo3, eixo4):
        self.eixo1 = eixo1
        self.eixo2 = eixo2
        self.eixo3 = eixo3
        self.eixo4 = eixo4
       
        self.lista_movimento.append(eixo1)
        self.lista_movimento.append(eixo2)
        self.lista_movimento.append(eixo3)
        self.lista_movimento.append(eixo4)

        print(self.lista_movimento)
robo = Robo()

robo.posicao(23, 45, 54,3)
robo.posicao(23, 45, 54,3)