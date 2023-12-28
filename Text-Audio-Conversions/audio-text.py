import base64
from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file(r"C:\Users\thetr\Documents\chucklenuts.mp3", format="mp3")

# Convert the audio to a base64-encoded string
audio_base64 = base64.b64encode(audio.export(format="wav").read()).decode()

# Print the base64-encoded string
with open("audioString.txt", "w") as f:
    f.write(audio_base64)