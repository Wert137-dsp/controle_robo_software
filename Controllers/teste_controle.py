#Publisher MQTT

import paho.mqtt.client as mqtt

# Definir o broker MQTT e a porta
broker = "test.mosquitto.org"
port = 1883
topic = "sic/topic"

# Função chamada quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker com sucesso!")
    else:
        print("Falha ao conectar, código de retorno: ", rc)

# Função chamada quando uma mensagem é publicada
def on_publish(client, userdata, mid):
    print("Mensagem publicada com sucesso!")

# Criar um cliente MQTT
client = mqtt.Client()

# Ligar as funções de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Conectar ao broker MQTT
client.connect(broker, port, 60)

# Iniciar o loop num thread separado para manter a conexão ativa
client.loop_start()

# Solicitar ao utilizador que escreva uma mensagem
while True:
    mensagem = input("Escreve a mensagem a enviar (ou 'sair' para terminar): ")
    if mensagem.lower() == 'sair':
        print("Encerrando o programa.")
        break
    # Publicar a mensagem no tópico
    client.publish(topic, mensagem)

# Parar o loop e desconectar o cliente MQTT
client.loop_stop()
client.disconnect()
