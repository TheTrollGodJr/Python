import speech_recognition as sr
from os import startfile
import os

dir = os.path.dirname(os.path.abspath(__file__))

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


while True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    recog = recognize_speech_from_mic(recognizer, microphone)
        
    word = "{}".format(recog["transcription"])

    if word.lower() == "open the app":
        try:
            startfile(startfile(os.path.join(dir, "app.pyw")))
        except:
            pass
        #break