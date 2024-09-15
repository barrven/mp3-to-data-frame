from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load MP3 file
audio = AudioSegment.from_mp3("sample-9s.mp3")

# Get raw audio data as an array of samples
samples = np.array(audio.get_array_of_samples())

# Create time values for plotting (in seconds)
time = np.linspace(0, len(samples) / audio.frame_rate, num=len(samples))

# Plot waveform
plt.figure(figsize=(12, 6))
if audio.channels == 2:
    # Stereo: plot left and right channels separately

    left_channel = samples[::2]
    right_channel = samples[1::2]
    
    df = pd.DataFrame({
        'left_channel': left_channel,
        'right_channel': right_channel
    })
    
    plt.plot(time[::2], left_channel, label="Left Channel", alpha=0.7)
    plt.plot(time[1::2], right_channel, label="Right Channel", alpha=0.7)

else:
    # Mono: plot a single channel
    df = pd.DataFrame({
        'mono_channel': samples
    })

    plt.plot(time, samples, label="Mono Channel")
    
print(df)

plt.title("Waveform of the MP3 file")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()