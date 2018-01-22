import numpy as np
from scipy.fftpack import fft,fftfreq,ifft
from scipy.io import wavfile
fs, data = wavfile.read('sheep.wav')
data_norm=data*1./abs(data).max()
t=np.arange(0,len(data)*1./fs,1/(fs*1.))
n_t=len(data)
dt=1/(fs*1.)
freq=fftfreq(n_t,1/(fs*1.))
c=fft(data_norm[:,0])
freq_cut = 500
c[abs(freq) > freq_cut] = 0
clean_f = ifft(c) 
wavfile.write('sheep_f.wav',fs,np.real(clean_f))