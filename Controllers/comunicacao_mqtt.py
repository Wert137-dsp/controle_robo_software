import paho.mqtt.client as mqtt

class comunicacaoMqtt:
    def __init__(self, broker = "broker.mqtt.cool", port = 1883):
        self.broker = broker
        self.port = port
        self.topic = "comandos/topic"
        self.client = mqtt.Client()

        print(self.client._client_id)

        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
               
        if rc == 0:
            print("Conectado ao broker com sucesso!")
            self.client.subscribe(self.getTopic())
        else:
         print("Falha ao conectar, código de retorno: ", rc)
            
    # Função chamada quando uma mensagem é publicada
    def on_publish(self, client, userdata, mid):
        print("Mensagem publicada com sucesso!")

    def on_message(self, client, userdata, msg):
        print(f" {msg.topic}: {msg.payload.decode()}")
    
    def desconectar(self):
        self.client.loop_stop()
        self.client.disconnect()
    
    def enviar_comando(self, message):
        self.client.publish(self.getTopic(), message)
       
    
    def conectar(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()
    

    def setTopic(self, topic):
        self.topic = topic
    def getTopic(self):
        return self.topic
        