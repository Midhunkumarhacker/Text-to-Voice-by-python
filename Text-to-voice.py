import pyttsx3
b=input("What voice you want - jarivs or friday : ")
if b=="jarvis":
    engine=pyttsx3.init('sapi5')
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
else:
    engine=pyttsx3.init('sapi5')
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)   


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Enter what i read for you")    
a=input("Enter word to speak",)    
speak(a)