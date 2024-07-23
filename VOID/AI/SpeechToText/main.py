import librosa
import librosa.display
import librosa.feature
import numpy as np
import os

# load audio data
def setSampleRate(filePath, targetSampleRate=16000):
    #audio, sr = librosa.load(filePath, targetSampleRate) # set new sampling rate for the data -- set to 16000 by default
    audio, sr = librosa.load(filePath, sr=targetSampleRate)
    return audio, sr # return data

# format transcriptions
def extractTranscription(filePath):
    # open transcription file and readlines
    with open(filePath, "r") as f:
        data = f.readlines()
    
    # list for new transcriptions
    transcriptions = []

    # format new data
    for item in data:
        transcriptions.append([item.split("|")[0].strip(), item.split("|")[1].strip()])
    
    #return data
    return transcriptions

def extractMelSpectro(audio, samplingRate=16000, n_mels=128):
    melSpectrogram = librosa.feature.melspectrogram(audio, sr=samplingRate, n_mels=n_mels)
    logMelSpectrogram = librosa.power_to_db(melSpectrogram, ref=np.max)
    return logMelSpectrogram

# loads all audio files into a list that is returned
def loadAudio(folderPath):
    # make a list of all files in folderPath
    files = [file for file in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, file))]

    # remove all files except .wav files
    for items in files[:]:
        if ".wav" not in items:
            files.remove(items)

    # create list to put formatted audio data in
    audioData = []

    # call setSampleRate to format audio, then append it to audioData
    for items in files:
        audio, sr = setSampleRate(f"{folderPath}{items}")
        audioData.append(audio)

    return audioData

if __name__ == "__main__":
    #print(extractTranscription("VOID/SpeechToText/data.txt"))
    ("Void/SpeechToText/audio/")