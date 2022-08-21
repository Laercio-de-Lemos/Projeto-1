from email.mime import audio
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print('Say something: ')
    audio = recognizer.listen(source) 

words = input('Saying something: ').lower()

if 'hello' in words:
    print("Hello to you too!")
elif 'how are you' in words:
    print('i am well, thanks')
elif 'goodbye' in words:
    print('Goodbye to you too!')
else:
    print('Huh?')        

print('You said:')
print(recognizer.recognize_google(audio))       