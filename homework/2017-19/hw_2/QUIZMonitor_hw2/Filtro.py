import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

rate, data = read("violin.wav")

fft = np.fft.rfft(data)
freq = np.fft.rfftfreq(len(data), 1/rate)

def bandpass(data, freq, f0 = 1e3, f1 = 2e3):
    fft = data.copy()
    pos = (freq > f0) & (freq < f1)
    pos = np.logical_not(pos)
    fft[pos] = 0
    return fft

filtered = bandpass(fft, freq)

fig, axes = plt.subplots(2, sharex=True)
axes[0].plot(freq, abs(fft), label="Original")
axes[1].plot(freq, abs(filtered), label="Bandpass")
axes[0].set_ylabel("$|\mathcal{F}|$")
axes[1].set_ylabel("$|\mathcal{F}|$")
axes[0].set_xlabel("Frequency (Hz)")
fig.savefig("ViolinFiltro.pdf")
