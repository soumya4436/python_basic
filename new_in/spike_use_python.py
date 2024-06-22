import pyttsx3
d=input("enter hat you say: ")
a=pyttsx3.init()
a.say(d)
a.runAndWait()