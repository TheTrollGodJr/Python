import base64
import io
from pydub import AudioSegment
from pydub.playback import play

with open("C:/Users/thetr/Documents/Python/audioString.txt", "r") as f:
    string = f.read()

# Base64-encoded audio data (replace this with your base64 string)
audio_base64 = string

# Decode the base64 audio data
audio_data = base64.b64decode(audio_base64)

# Load the audio data as an AudioSegment
audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")

# Play the audio
play(audio)
