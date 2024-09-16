import sys
import os
from Models import Programa, Posicao
from Controllers import comunicacaoMqtt



pos1 = Posicao()
pos1.posicao(314, 514, 1030, 1240)

pos2 = Posicao()
pos2.posicao(34, 54, 100, 120)

prog1 = Programa()
prog1.adicionar_passo(pos1.lista_movimento)
prog1.adicionar_passo(pos2.lista_movimento)

passos = prog1.executar_programa()

for passo in range(len(passos)):
    print(passos[passo])
