import sys
import os

from flask import Flask, render_template, url_for, session, redirect, request
import paho
import secrets
import time
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models import Programa, Posicao, Delay, Robo

from Controllers import comunicacao_mqtt as cmqtt

mqt = cmqtt.comunicacaoMqtt()

def tred_mqtt():
    mqt.conectar()


def teste():
    while True:
        time.sleep(1)
        mqt.enviar_comando(input("Digite um comando: "))

def webPage():

    app = Flask(__name__)

    app.secret_key = secrets.token_hex(16)

    print(app.secret_key)

    @app.route("/")
    def index():

      
            return render_template("index.html")

    @app.route("/cadastrar", methods=['GET', 'POST'])
    def cadastrar():
        
        if request.method == "POST":
            
            nome = request.form.get("nome_cad")
            email = request.form.get("email_cad")
            senha = request.form.get("pass_cad")
        
        return redirect("/")

    @app.route("/login", )
    def login():
        if "email" not in session:
            return render_template("login_cadastro.html")
        else:
            return redirect("/")
        
    app.run()
   

mqtt_tred = threading.Thread(target=tred_mqtt)
mqtt_tred.start()

thred1 = threading.Thread(target=teste)
thred1.start()











try:
    webPage()
    while True:
        time.sleep(1)
except KeyboardInterrupt:   
    mqt.desconectar()
    mqtt_tred.join()
    thred1.join()

'''


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
    
'''