import sounddevice as sd
import wavio as wv
import config
import whisper
import os, glob

freq = 44100
duration = 5 # in seconds
binary = False

print('Recording')

def record():
    global binary
    #while True:
    if binary:
        filename = "1"
    else:
        filename = "0"

    # Start recorder with the given values of duration and sample frequency
    # PTL Note: I had to change the channels value in the original code to fix a bug
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()

    # Convert the NumPy array to audio file
    wv.write(f"C:/Users/thetr/Documents/Python/openaiChatAssistant/recordings/{filename}.wav", recording, freq, sampwidth=1)

    if binary:
        binary = False
    else:
        binary = True
