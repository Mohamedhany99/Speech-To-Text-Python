import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print("say smth")
    audio =r.listen(source)
    print(audio)

try:
    print("analysing")
    text=r.recognize_google(audio)
    print("you said : ",text)
except:
    print("failed")
