import sys
import os

from flask import Flask, render_template, url_for, session, redirect, request, jsonify
import paho
import json
import secrets
import time
import threading
from queue import Queue
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models import Programa, Posicao, Delay, Robo

from Controllers import comunicacao_mqtt as cmqtt
from Controllers import conexao_bd
from Controllers.assistente_virtual import *


mqt = cmqtt.comunicacaoMqtt()

def tred_mqtt():
    mqt.conectar()


def teste():
    while True:
        time.sleep(1)
        mqt.enviar_comando(input("Digite um comando: "))


def executarPosicao(nome):

        sql = "select eixoA, eixoB from posicao where nome = %s"

        conexao_bd.cursor.execute(sql, (nome,))
        colunas = conexao_bd.cursor.column_names
        result = [dict(zip(colunas, linhas)) for linhas in conexao_bd.cursor.fetchall()]
        print(result)

      

        print(result)
        mqt.enviar_comando(json.dumps(result[0]))
# Função para processar a fila de fala

fala_queue = Queue()
def processar_fala():
    while True:
        mensagem = fala_queue.get()  # Pega a mensagem da fila
        if mensagem is None:
            break  # Se a mensagem for None, o loop termina
        engine.say(mensagem)
        engine.runAndWait()

# Inicia o thread que vai processar a fila de fala
thread_fala = threading.Thread(target=processar_fala)
thread_fala.daemon = True
thread_fala.start()


# Função que processa o comando de voz
def checar_comando():
    try:
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ajustando para ruído ambiente...")
            mic.adjust_for_ambient_noise(source)
            print("Pronto, pode falar.")
            audio = mic.listen(source)

        # Processar o comando de voz
        frase = mic.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {frase}")

        # Usar expressão regular para capturar o comando e nome
        match = re.search(r'\b(Executar|Faça)\b\s+([A-Za-z]+)\s*(\d+)?', frase, re.IGNORECASE)
        if match:
            acao = match.group(1)  # "Executar" ou "Faça"
            nome_comando = match.group(2).strip()  # Nome do comando (ex: "Movimento")
            num = match.group(3) if match.group(3) else "0"  # Número opcional

            print(f"Ação: {acao}, Nome do comando: {nome_comando}, Número: {num}")

            # Conectar ao banco de dados e verificar se o comando existe
            try:

                
                sql = "SELECT nome FROM posicao WHERE nome = %s"
                conexao_bd.cursor.execute(sql, (nome_comando + num,))
                if conexao_bd.cursor.fetchone():  # Verifica se encontrou um comando correspondente
                    executarPosicao(nome_comando + num)
                    fala_queue.put(f"Executando {nome_comando + num}")
                else:
                    fala_queue.put("Comando não encontrado.")
            except:
                print(f"Erro ao conectar ao banco de dados: ")
                fala_queue.put("Erro ao acessar o banco de dados.")

        else:
            print("Comando inválido ou não reconhecido.")
            fala_queue.put("Comando inválido ou não reconhecido.")

    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        fala_queue.put("Não consegui entender o que você disse.")
    except sr.RequestError as e:
        print(f"Erro de serviço de reconhecimento: {e}")
        fala_queue.put(f"Erro de serviço de reconhecimento: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        fala_queue.put(f"Erro inesperado: {e}")

        

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
    '''
    @app.route("/enviarEixo", methods=["POST"])
    def receberEixo():
        dados = request.json
        print(dados.get("eixoA")+": "+dados.get("valor"))
        mqt.enviar_comando(dados)
        return jsonify({"message": "Eixo recebido"}), 200
    '''
    @app.route("/salvarPosicao", methods = ["POST"])
    def salvarPosicao():
        dados = request.json

        posicao = Posicao()
        posicao.posicao(dados.get("nome"), dados.get("eixoA"), dados.get("eixoB"))
        
        sq = "select * from posicao where nome = %s"
        valores = (dados.get("nome"),)
        conexao_bd.cursor.execute(sq, valores)

        dic = conexao_bd.cursor.fetchall()


        if len(dic) == 0:

            sql = "insert into posicao(nome, eixoA, eixoB)values(%s,%s,%s)"
            
            valores = (dados.get("nome"), dados.get("eixoA"), dados.get("eixoB"))
            conexao_bd.cursor.execute(sql, valores)
            
            conexao_bd.conexao.commit()
        
            print(valores)
            print(posicao.get_lista_movimento())

            return jsonify({"message": "Salvo"}), 200
        else:
            print("Nome de posição já salva")
            return jsonify({"message": "Nome da posição já salva"}), 400


    @app.route("/enviarEixo", methods = ["POST"])
    def enviarEixo():

        dados = request.json
        
        print(dados)
        mqt.enviar_comando(json.dumps(dados))

        return jsonify({"message": "Ok"}), 200 
    

    @app.route("/moverRobo", methods = ["POST"])
    def moverRobo():

        dados = request.json
        
        print(dados)
        mqt.enviar_comando(json.dumps(dados))

        return jsonify({"message": "Ok"}), 200 
    
    @app.route("/getPosicoes", methods = ["POST"])
    def getPosicoes():

        conexao_bd.cursor.execute("select id_posicao, nome, eixoA, eixoB from posicao")
        colunas = conexao_bd.cursor.column_names
        result = [dict(zip(colunas, linhas)) for linhas in conexao_bd.cursor.fetchall()]
        print(result)
        return jsonify(result)
    
    @app.route("/checarComando", methods=["POST"])
    def checar_comando_api():
        # Cria uma thread para executar a escuta do comando sem bloquear a resposta do Flask
        thread = threading.Thread(target=checar_comando)
        thread.start()

        # Retorna uma resposta rápida, enquanto o comando de voz está sendo processado
        return jsonify({"message": "Comando de voz sendo processado"}), 200
            
            
    
         
    
      

    app.run()


mqtt_tred = threading.Thread(target=tred_mqtt)
mqtt_tred.start()

thred1 = threading.Thread(target=teste)
#thred1.start()

#thred_assistente = threading.Thread(target=checar_comando)
#thred_assistente.daemon = True  # Garante que o thread será encerrado com o programa principal
#thred_assistente.start()

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