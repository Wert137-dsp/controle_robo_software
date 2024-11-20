import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models import Posicao
import conexao_bd

class BancoPosicao:

    def __init__(self):
        self.posicao = Posicao()

    def adicionarPosicao(self, posicao):
        
        self.posicao = posicao

        

    def atualizarPosicao(self):
        pass
    def deletarPosicao(self):
        pass
    def visualizarPosicaos(self):
        pass
    def visualizarPosicaoUnico(self):
        pass