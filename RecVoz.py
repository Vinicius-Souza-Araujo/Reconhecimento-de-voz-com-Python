# Antes de rodar o código instale as seguintes bibliotecas: SpeechRecognition e  PyAudio.

#Começo do código.

#Importe a biblioteca abaixo:
import speech_recognition as sr

#Variável que reconhece a voz.
reconhecedor =  sr.Recognizer()

#Utilizando a estrutura do with abrimos o microfone e quando a variável armazenar as voz e exibi-la o programa termina.
with sr.Microphone() as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    print ('Pode falar: ...')

    #Recebe sua voz.
    audio = reconhecedor.listen(mic)

    #Reconhece e transforma a voz em texto.
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print (texto)

#Fim do código.
