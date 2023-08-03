import shutil
import librosa
import soundfile as sf
import taglib

f = open("C:/Users/thetr/Documents/Python/Glados/filenames.txt", "r")
info = f.readlines()
f.close()

for items in info:
    num = items.split("|")[1].split("\n")[0]
    file = items.split("|")[0]

    filePath = fr"C:\Users\thetr\Documents\Glados\wavs\{num}.wav"

    #os.rename(f"C:/Users/thetr/Documents/Glados/original/{file}.wav", f"C:/Users/thetr/Documents/Glados/wav/{num}.wav")
    shutil.copy2(f"C:/Users/thetr/Documents/Glados/original/{file}.wav", filePath)

    y, sr = librosa.load(filePath, sr=22050)
    trimmed_audio, _ = librosa.effects.trim(y, top_db=20)
    normalized_audio = librosa.util.normalize(trimmed_audio)
    sf.write(filePath, normalized_audio, sr, subtype='PCM_16')
    
    wav = taglib.File(filePath)
    wav.tags["TITLE"] = [f"{num}"]
    wav.tags["TRACKNUMBER"] = [f"{num}"]
    wav.save()

    print(file, num)