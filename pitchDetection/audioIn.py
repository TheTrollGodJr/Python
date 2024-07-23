import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

RATE = 64000
CHUNK = 1024

all_pitches = []

def empty_frame(length):
    """Returns an empty 16bit audio frame of supplied length."""
    frame = np.zeros(length, dtype='i2')
    return to_raw_data(frame)

def to_int_data(raw_data, num_channels):
    """Converts raw bytes data to numpy array."""
    data = np.frombuffer(raw_data, dtype=np.int16)
    if num_channels == 2:
        data = data.reshape(-1, 2)
        data = data.mean(axis=1).astype(np.int16)
    return data

def to_raw_data(int_data):
    data = int_data.clip(-32678, 32677)
    data = data.astype(np.dtype('i2'))
    return data.tobytes()

def resample_audio(data, original_rate, target_rate):
    """Resamples the audio data to the target sample rate."""
    num_samples = int(len(data) * (target_rate / original_rate))
    resampled_data = resample(data, num_samples)
    return resampled_data.astype(np.int16)

def process(raw_data, num_channels, original_rate):
    data = to_int_data(raw_data, num_channels)
    if original_rate != RATE:
        data = resample_audio(data, original_rate, RATE)
    data = data * 4  # raise volume
    detect_pitch(data)
    return to_raw_data(data)

def normal_distribution(w):
    width = w + 1
    weights = np.exp(-np.square([2 * x / width for x in range(width)]))
    weights = np.pad(weights, (width - 1, 0), 'reflect')
    weights = weights / np.sum(weights)
    return weights

def detect_pitch(int_data):
    if 'avg' not in detect_pitch.__dict__:
        detect_pitch.avg = 0
    WIND = 10
    CYCLE = 400
    weights = normal_distribution(WIND)
    windowed_data = np.pad(int_data, WIND, 'reflect')
    smooth_data = np.convolve(int_data, weights, mode='valid')
    smooth_pitches = [0] + [np.mean(smooth_data[:-delay] - smooth_data[delay:]) for delay in range(1, CYCLE)]

    dips = [x for x in range(WIND, CYCLE - WIND) if smooth_pitches[x] == np.min(smooth_pitches[x - WIND:x + WIND])]
    if len(dips) > 1:
        av_dip = np.mean(np.ediff1d(dips))
        cheq_freq = RATE / av_dip
        detect_pitch.avg = detect_pitch.avg * 0.5 + cheq_freq * 0.5
        all_pitches.append(int(detect_pitch.avg))
        print('\r' + str(int(detect_pitch.avg)) + ' Hz        ', end='')

def main(audio_file):
    with wave.open(audio_file, 'rb') as wf:
        num_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        original_rate = wf.getframerate()
        
        assert sampwidth == 2  # Ensure 16-bit samples

        while True:
            data = wf.readframes(CHUNK)
            if len(data) == 0:
                break
            process(data, num_channels, original_rate)

    plt.plot(all_pitches)
    plt.show()

if __name__ == "__main__":
    #audio_file = "pitchDetection/audio/DreamOn.wav"  # specify your audio file path here
    audio_file = "D:/Downloads/arthur.wav"
    main(audio_file)






#"pitchDetection/audio/DreamOn.wav"