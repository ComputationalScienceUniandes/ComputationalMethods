import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


rate, do = wav.read('Do.wav')
rate, sol = wav.read('Sol.wav')

def frequency(n, d = 1.0):
    f = np.arange(0, n//2 + 1)/(d*n)
    return f

def dft(data):
    N = len(data)
    dt= 1./data[0]
    n = np.arange(0, N)
    transform = np.zeros(N//2 + 1, dtype=complex)
    for k in range(transform.shape[0]):
        transform[k] = (data*np.exp(-1j*2*np.pi*k*n/N)).sum()
    return transform

def maxfilter(data, freq, df = 50):
    fft = data.copy()
    pos = abs(fft).argmax()
    if pos-df < 0:
        fft[0: pos+df] = 0
    else:
        fft[pos-df: pos+df] = 0

    return fft

def savewav(name, rate, data):
    data = data.astype(np.int16)
    wav.write(name, rate, data)

def lowpass(data, freq, c = 1000):
    fft = data.copy()
    fft[freq > c] = 0
    return fft

# trans_do = dft(do)
# trans_sol = dft(sol)
trans_do = np.fft.rfft(do)
trans_sol = np.fft.rfft(sol)

freq_do = frequency(do.shape[0], d=1.0/rate)
freq_sol = frequency(sol.shape[0], d=1.0/rate)

trans_max = maxfilter(trans_do, freq_do)
trans_low = lowpass(trans_do, freq_do)

ys = [trans_do, trans_max, trans_low]
labels = ["Original", "Max filter", "Low pass"]
fig, axes = plt.subplots(3, sharex=True)

fy = EngFormatter()
fx = EngFormatter(unit='Hz')
for i in range(len(ys)):
    axes[i].plot(freq_do, abs(ys[i]), label=labels[i])
    axes[i].set_ylabel("$|\mathcal{f}|$")
    axes[i].yaxis.set_major_formatter(fy)

axes[-1].set_xlabel('Frequency')
axes[-1].xaxis.set_major_formatter(fx)
fig.tight_layout()
fig.savefig("DoFiltros.pdf")

factor = 391.0/260.0

fig, ax = plt.subplots()
ax.plot(freq_do*factor, abs(trans_do), label="New Do")
ax.plot(freq_sol, abs(trans_sol), label = "Sol")
ax.set_xlabel("Frecuency")
ax.set_ylabel("$|\mathcal{F}|$")
ax.xaxis.set_major_formatter(fx)
ax.yaxis.set_major_formatter(fy)
fig.savefig("DoSol.pdf")

dopico = np.fft.irfft(trans_max)
dolow = np.fft.irfft(trans_low)

savewav("Do_pico.wav", rate, dopico)
savewav("Do_pasabajos.wav", rate, dolow)
savewav("DoSol.wav", int(factor*rate), do)
