import sounddevice as sd
import wavio as wv
import whisper
import os
import threading

freq = 44100
duration = 5 # in seconds
binary = False
run = False
stop = False

def transcribe():
    global run
    global stop
    while True:
        if run:
            print("started")
            run = False
            model = whisper.load_model("base")

            if binary:
                filename = "C:/Users/thetr/Documents/Python/openaiChatAssistant/recordings/0.wav"
            else:
                filename = "C:/Users/thetr/Documents/Python/openaiChatAssistant/recordings/1.wav"

            print(filename)

            if os.path.exists(filename):
                audio = whisper.load_audio(filename)
                audio = whisper.pad_or_trim(audio)
                mel = whisper.log_mel_spectrogram(audio).to(model.device)
                options = whisper.DecodingOptions(language= 'en', fp16=False)

                result = whisper.decode(model, mel, options)
                print(result)

                if result.no_speech_prob < 0.5:
                    if ("whisper, stop" in result.text.lower()) or ("whisper stop" in result.text.lower()):
                        stop = True
                        break

                    #print(result.text)

                    # append text to transcript file
                    with open("C:/Users/thetr/Documents/Python/openaiChatAssistant/transcription.txt", 'a') as f:
                        f.write(result.text + "\n")
                print("ended")

def record():
    global binary
    global run
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    while True:
        if stop:
            break

        if binary:
            filename = "1"
        else:
             filename = "0"

        #print(filename)

        # Record audio for the given number of seconds
        sd.wait()

        # Convert the NumPy array to audio file
        wv.write(f"C:/Users/thetr/Documents/Python/openaiChatAssistant/recordings/{filename}.wav", recording, freq, sampwidth=2)

        if binary:
            binary = False
        else:
            binary = True
        
        run = True


with open("C:/Users/thetr/Documents/Python/openaiChatAssistant/transcription.txt", 'w') as f:
    f.write("")

t1 = threading.Thread(target=transcribe)
t2 = threading.Thread(target=record)
t1.start()
t2.start()
t1.join()
print("t1")
t2.join()
print("t2")

print("all joined")