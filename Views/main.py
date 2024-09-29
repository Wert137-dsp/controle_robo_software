import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models import Programa, Posicao, Delay, Robo

print("Sistema de controle de robo: ")

decisao = 0

robo1 = Robo()

while decisao != 5:


    decisao = abs(int(input("Escolha uma opção: (1- Criar programa, 2- criar movimento, 3, 4, 5 - sair): ")))
    

    if decisao == 1: 

        prog1 = Programa()
        
        #nome_robo = input("Digite o nome do robo: ")
        prog1.set_nome(input("Digite o nome do programa: "))
        prog1.set_descricao(input("Descrição: "))

        robo1.adicionar_programa(prog1.get_nome(), prog1.get_descricao(), prog1.get_programa())

        print(robo1.pegar_programa())
    
