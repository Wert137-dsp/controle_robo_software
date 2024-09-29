
class Robo():
    def __init__(self):
        #super.__init__(nome, token)
        self.lista_programas = []

    def adicionar_programa(self, nome_programa, descricao , conteudo):
        self.lista_programas.append({"nome_programa": nome_programa, "descricao" : descricao, "conteudo": conteudo})
    
    def pegar_programa(self, ind = 0):

        if ind == 0:
            return self.lista_programas
        else:
            return self.lista_programas[ind-1]
    
    def deletar_programa(self, id_programa):
        self.lista_programas.pop(id_programa)

    def executar_programa(self, id_programa):
        pass
    
    def visualizar_programa(self, id_programa):
        pass

    def ver_lista_programas():
        pass