from Models.Posicao import Posicao

class Programa():

    def __init__(self):
        self.passos = []

    def executar_programa(self):
        for passo in self.passos:
            print(passo)

    def adicionar_passo(self, posicao):
        self.passos.append(posicao)
