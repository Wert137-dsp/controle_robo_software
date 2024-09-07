import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from Models.Programa import Programa
from Models.Posicao import Posicao

pos1 = Posicao()
pos1.posicao(314, 514, 1030, 1240)

pos2 = Posicao()
pos2.posicao(34, 54, 100, 120)

prog1 = Programa()
prog1.adicionar_passo(pos1.lista_movimento)
prog1.adicionar_passo(pos2.lista_movimento)

prog1.executar_programa()