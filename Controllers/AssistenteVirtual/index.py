import speech_recognition as sr
import re
import pyttsx3
## isso aq importa os drivers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Defina o caminho para o OperaDriver baixado
caminho_operadriver = r"C:\Users\alexa\Downloads\operadriver_win64\operadriver_win64.exe"

# Configurações opcionais para o OperaDriver (se necessário)
opera_options = Options()
# Se necessário, especifique o caminho para o executável do Opera (caso o Selenium não encontre automaticamente)
# Exemplo para Windows, substitua pelo seu caminho correto, se necessário
opera_options.binary_location = r"C:\Program Files\Opera\launcher.exe"


# variavel nome, para conseguir identificar o usuário
nome = ""
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")

while True:
    # acha o microfone disponivel
    mic = sr.Recognizer()
    # tipo um if, usando o microfone e define ele como uma fonte
    with sr.Microphone() as source:
        # faz ajuste no microfone e melhora o audio
        mic.adjust_for_ambient_noise(source)
        print("Vamos começar, fale alguma coisa...")
        # define que o audio vai ser tudo que o microfone pegar, tendo em base a source
        audio = mic.listen(source)
        #um pequeno trycath
        try:
            # a frase vai levar em conta a ia do google de reconhecimento de voz, em base a linguagem PT BR
            frase = mic.recognize_google(audio, language='pt-BR')

            # Detecção de "ajudar", ou seja, um filtro
            if re.search(r'\bajudar\b', frase, re.IGNORECASE):
                engine.say("Ajuda")
                engine.runAndWait()
                print("Algo relacionado a ajuda.")

            # Detecção de "meu nome é"
            elif re.search(r'\bmeu nome é\b', frase, re.IGNORECASE):
                t = re.search(r'meu nome é (.*)', frase, re.IGNORECASE)
                if t:
                    nome = t.group(1).split()[0]  # Pega apenas o primeiro nome, se houver mais
                    print("Seu nome é " + nome)
                    engine.say("Nome falado foi " + nome)
                    engine.runAndWait()
            
                #tentativa de comando para abrir navegador, ainda nao funciona pq eu tenho que colocar o navegador certo
            elif re.search(r'\babrir o navegador\b', frase, re.IGNORECASE):
                print("Abrindo o navegador.")
                engine.say("Abrindo o navegador.")
                engine.runAndWait()

                # Inicializar o navegador Opera
                navegador = webdriver.Opera(executable_path=caminho_operadriver, options=opera_options)
                navegador.get("https://www.google.com")


            # Comando para parar o loop
            elif re.search(r'\bparar\b', frase, re.IGNORECASE):
                print("Parando o sistema.")
                engine.say("Parando o sistema.")
                engine.runAndWait()
                break
            print("Você falou: " + frase)        
            # a maioria de tratamento de erros plausiveis.
        except sr.UnknownValueError:
            print("Ops, não consegui entender o que foi dito.")
        except sr.RequestError as e:
            print(f"Erro na requisição ao serviço de reconhecimento de fala: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
