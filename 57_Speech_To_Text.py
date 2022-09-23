# Speech to text
import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

# print(voices[1].id)

engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get():
    r = sr.Recognizer()
