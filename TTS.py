from gtts import gTTS
import tkinter as tk
from playsound import playsound
import speech_recognition as sr
import os
import tempfile

#SpeechRecognition
def reconocimientoDeVoz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-MX")
        return text
    except sr.UnknownValueError:
        return "No se entendio el audio"
    except sr.RequestError as e:
        return "Error de request {0}".format(e)

#TTS
def tts():
    texto = reconocimientoDeVoz()
    print(texto)

    tts = gTTS(text=texto, lang="es")
    # audio = "audio.mp3"
    # tts.save(audio)
    # playsound(audio)
    path = tempfile.gettempdir() + "\\audio.mp3"
    tts.save(path)
    playsound(path)

#GUI
gui = tk.Tk()
gui.title("VtTTS")
gui.geometry("320x240")

# frame = tk.Frame(gui)
# frame.pack(expand=True, fill="both")

button = tk.Button(gui, text="Iniciar Reconocimiento",command=tts)
button.place(relx=0.5, rely=0.5, anchor="center")

gui.mainloop()