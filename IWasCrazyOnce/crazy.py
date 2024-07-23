import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import time

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
    time.sleep(.01)
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    recog = recognize_speech_from_mic(recognizer, microphone)
         
    word = "{}".format(recog["transcription"])
    print(word)

    if "crazy" in word.lower():
        break

audio = AudioSegment.from_file("C:/Users/thetr/Documents/Python/IWasCrazyOnce/rats.mp3")

while True:
    play(audio)
    time.sleep(599)