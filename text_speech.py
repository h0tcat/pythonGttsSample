from gtts import gTTS
import sys
import os

if(len(sys.argv)==3):
    speechText=sys.argv[1]
    speechLanguage=sys.argv[2]
    
    speechData=gTTS(text=speechText,lang=speechLanguage)

    speechData.save("voice.mp3")
    os.system("mpg321 voice.mp3")
    os.remove("voice.mp3")
else:
    print("Usage: text_speech text speech_language")