import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything...")
    audio= r.listen(source)

    try:
        text=r.recognize_google(audio)
        if text.lower() in ["hello","hey","hola"]:
            print("Hello user how are you?")
        else:
            print("{}".format(text))
        
    except:
        print("sorry could not recognize your voice")
