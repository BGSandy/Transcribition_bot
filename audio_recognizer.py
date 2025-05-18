import speech_recognition as sr
import random
from googletrans import Translator
translator = Translator()
translated = translator.translate(next, dest='en')  # здесь 'en' — это английский
print("🌍 Перевод на английский:", translated.text)
lang = input("Введите код языка для перевода (например, 'en' — английский, 'es' — испанский): ")

words_by_level = {
    "easy": ["кот", "собака", "апельсин", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "речь", "воображение"]
}
recognized = recognized.lower()
random.choice(words_by_level["easy","medium","hard"])
def recognize_speech():
    recog = sr.Recognizer()
    mic = sr.Microphone()\
    
    with sr.Microphone() as input_stream:
        recog.adjust_for_ambient_noise(input_stream)
        print("Начни говорить") #временная строка
        audio = recog.listen(input_stream)
        return recog.recognize_google(audio, language ='ru-RU')#en-EN\
transcribed_speech = recognize_speech()#временная строка\
print(f'Google Speech Recognation думает, что ты сказал следующее: {transcribed_speech}')#временная строка
