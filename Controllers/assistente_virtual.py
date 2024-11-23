import speech_recognition as sr
import re
import pyttsx3
import nltk
import gensim

import string
import time


comandosajuda = [['ajudar', 'ajuda'], ['socorrer', 'socorro'], ['auxiliar', 'auxilie']]
comandosparar = [['parar', 'para'], ['desligue', 'pare'], ['desative', 'desativar']]
comandosacoes = [['movimente', 'mova'], ['mover'], ['movimentar', 'mexer']]
criacaocomando = [['criar', 'crie'], ['faça', 'fazer'], ['gerar', 'gere'], ['formar', 'forme']]
comandosdeafirmacao = [['sim'], ['não'], ['desejo', 'confirmo'], ['quero']]



lista_num = []
valorlistamax = 0.00
ControleDeMovimentos = 0

comando = ""
nome = ""
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")



def chamar_assistente():
     mic = sr.Recognizer()


def iniciar_assistente():
   while True:
    print("Esperando comando")
    # acha o microfone disponivel
    mic = sr.Recognizer()

    # tipo um if, usando o microfone e define ele como uma fonte
    with sr.Microphone() as source:
        # faz ajuste no microfone e melhora o audio
        mic.adjust_for_ambient_noise(source)
        # define que o audio vai ser tudo que o microfone pegar, tendo em base a source
        audio = mic.listen(source)

    #um pequeno trycatch
    try:

        # a frase vai levar em conta a ia do google de reconhecimento de voz, em base a linguagem PT BR
        fraseInicial = mic.recognize_google(audio, language='pt-BR')

        if re.search(r'\bExecutar\b', frase1, re.IGNORECASE):
            comando = "executar"
            engine.say("Executando comando")
            engine.runAndWait()   

        if re.search(r'\bSexta-feira\b', fraseInicial, re.IGNORECASE):
           # engine.say(f"Olá Diego me chamo Sexta-Feira, sou sua assistente virtual integrada ao seu dispositivo robótico, agora, iremos iniciar a nossa interação, caso precise de ajuda, é só dizer")
           # engine.runAndWait()

            while True:
                print("123")
               # engine.say(f"O que deseja?")
               # engine.runAndWait()
                with sr.Microphone() as source:
                    # faz ajuste no microfone e melhora o audio
                    mic.adjust_for_ambient_noise(source)
                    # define que o audio vai ser tudo que o microfone pegar, tendo em base a source
                    audio = mic.listen(source)

                try:
                    
                    print("Teste")
                    frase1 = mic.recognize_google(audio, language='pt-BR')
                    
                    if re.search(r'\bExecutar\b', frase1, re.IGNORECASE):
                        comando = "executar"
                    engine.say("Executando comando")
                    engine.runAndWait()

                    if re.search(r'\bPare\b', frase1, re.IGNORECASE):
                        engine.say(f"Até logo")
                        engine.runAndWait()
                        break
                    
                except sr.UnknownValueError:
                    engine.say("Não consegui entender o que você disse.")
                    engine.runAndWait()
                except sr.RequestError as e:
                    engine.say("Erro ao acessar o serviço de reconhecimento")
                    engine.runAndWait()
        
        

    except:
        pass




