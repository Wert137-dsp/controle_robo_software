#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include "esp_task_wdt.h"


#define PWM_FREQ 50
#define RESOLUTION 12

const int pwmPins[7] = {2, 4, 5, 27, 26, 25, 33};
const int channel[7] = {0, 1, 2, 6, 3, 4, 5};

// Configurações da rede Wi-Fi
const char* ssid = "GreenV-IoT";
const char* password = "Greenv@135";

// Configurações do broker MQTT
const char* mqtt_server = "broker.mqtt.cool"; // Substitua pelo IP ou endereço do broker
const int mqtt_port = 1883;                    // Porta padrão MQTT
const char* mqtt_topic = "comandos/topic";     // Tópico para assinar

WiFiClient espClient;
PubSubClient client(espClient);

// Função chamada quando uma mensagem é recebida
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensagem recebida no tópico: ");
  Serial.println(topic);

  // Copiar o payload para uma string
  char message[length + 1];
  strncpy(message, (char*)payload, length);
  message[length] = '\0';

  Serial.print("Mensagem recebida (JSON): ");
  Serial.println(message);

  // Criação de um objeto JSON
  StaticJsonDocument<256> doc; // Ajuste o tamanho conforme necessário
  DeserializationError error = deserializeJson(doc, message);

  if (error) {
    Serial.print("Erro ao analisar JSON: ");
    Serial.println(error.c_str());
    return;
  }

  // Converter JSON para uma lista
  JsonArray array = doc.as<JsonArray>();
  
  String eixos[7] = {"A", "B", "C", "G", "D", "E", "F"};
  for(int i = 0; i < 2; i++){

    String eixoKey = "eixo" +eixos[i];
    
    if(doc.containsKey(eixoKey)){
      int valorEixo = doc[eixoKey];

      int valores_mapeados = map(valorEixo, 0, 4095, 0, 500);
      int duty = map(valores_mapeados, 0, 100, 0, 4095);
      Serial.println(ledcRead(channel[i]));
      if(ledcRead(channel[i]) < valores_mapeados){

          while(ledcRead(channel[i]) < valores_mapeados){
              int valor = ledcRead(channel[i]);
                  ledcWrite(channel[i], valor+=10);
                  Serial.println(ledcRead(channel[i]));

                  delay(100);
          }
          


      }else{

        while(ledcRead(channel[i]) > valores_mapeados){
              int valor = ledcRead(channel[i]);
                  ledcWrite(channel[i], valor-=10);
                  Serial.println(ledcRead(channel[i]));

                  delay(100);
          }

      }

      Serial.println(valores_mapeados);

    }
  }


 
}

void setup_wifi() {
  delay(10);
  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado.");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Tentando se conectar ao MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("Conectado ao broker MQTT!");
      client.subscribe(mqtt_topic); // Inscreve-se no tópico
    } else {
      Serial.print("Falha na conexão. Código de erro: ");
      Serial.println(client.state());
      delay(5000); // Tenta novamente após 5 segundos
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();

  esp_task_wdt_init(18000, true);
  esp_task_wdt_delete(NULL);
  
  for (int i = 0; i < 2; i++)
  {
    ledcSetup(channel[i], PWM_FREQ, RESOLUTION);
    ledcAttachPin(pwmPins[i], channel[i]);
  }
  

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() {
 if (!client.connected()) {
    reconnect();
  }
  esp_task_wdt_reset();
  client.loop();


  

 
}
