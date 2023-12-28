import base64
import io
from pydub import AudioSegment
from pydub.playback import play

def playAudio(inp):
    print("started")
    audio_data = base64.b64decode(inp)
    print("base64")
    audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
    print("converted")
    play(audio)
    print("playing")


with open("Text-Audio-Conversions/inp.txt", "r") as f:
    string = f.read()
    #print(string)
    playAudio(string)