from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio(input_file, output_folder):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Split on silence
    chunks = split_on_silence(audio, min_silence_len=250, silence_thresh=-40)

    # Save the chunks
    for i, chunk in enumerate(chunks):
        chunk.export(f"{output_folder}/chunk_{i}.wav", format="wav")

# Example usage
input_file = "D:/Downloads/void.wav"
output_folder = "C:/Users/thetr/Documents/Python/audioOutput"
split_audio(input_file, output_folder)
