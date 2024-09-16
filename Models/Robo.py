from Dispositivo import Dispositivo

class Robo(Dispositivo):
    def __init(self, nome, token):
        super.__init__(nome, token)
        self.lista_programas = []

    def adicionar_programa(self, prog):
        self.lista_programas.append(prog)
    
    def deletar_programa(self, id_programa):
        self.lista_programas.pop(id_programa)

    def executar_programa(self, id_programa):
        pass
    
    def visualizar_programa(self, id_programa):
        pass

    def ver_lista_programas():
        pass