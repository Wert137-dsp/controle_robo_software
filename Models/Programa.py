class Programa():

    def __init__(self):
        self.passos = []

    def executar_programa(self):
        for passo in self.passos:
            pass
        return self.passos
    def adicionar_passo(self, posicao):
        self.passos.append(posicao)
