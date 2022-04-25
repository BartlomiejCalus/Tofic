import speech_recognition as sr
import pyttsx3 as ffs
import pywhatkit
import wikipedia as wiki
import sys, time
import kivy

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='Hello world')

# potrzebne definicje
r = sr.Recognizer()
bot = ffs.init()
bot.setProperty('voice', bot.getProperty('voices')[0].id)


# mówinie bota
def speak(tekst):
    bot.say(tekst)
    bot.runAndWait()

# słuchanie komendy
def getText():
    with sr.Microphone() as sorc:
        audio = r.listen(sorc)
        text = r.recognize_google(audio, language="pl-PL")
        if text == "":
            return None
        else:
            return text

# szukanie słów kluczowych w nagraniu
def spr(string, szukane):
    return [element for element in szukane if element in string.lower()]


# deinicje szukanych fraz
WITAJ = ["tofik", "tofiku"]
YT = ["puść", "posłuchać"]
SZUKAJ = ["wyszukaj", "znajdź", "wygoogluj", "szukaj"]
WLACZ = ["włącz", "uruchom", "odpal"]
WIKI = ["wiki", "wikipedia", "wikipedii"]
KONIEC = ["spać", "uśpienie", "dobranoc"]


# obsługa Tofica
while False:
    time.sleep(0.5)
    print("Działam")
    temp = "Tofiki puść midowe lata"#getText()
    print(temp)
    print("" * 50, end='\r')
    if temp != None:
        if len(spr(temp, WITAJ)):
            print (temp)
            if len(spr(temp, KONIEC)):
                speak("Hau hau.")
                break
            elif len(spr(temp, WIKI)):
                fraza = temp.lower().split(spr(temp, WIKI)[0])[1]
                info = wiki.summary(fraza)
                speak(info[:400])
            elif len(spr(temp, YT)):
                fraza = temp.lower().split(spr(temp, WIKI)[0])[1]
                pywhatkit.playonyt(fraza)

MyApp().run()