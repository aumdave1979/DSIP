import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

N = 31  # number of filter coefficients (taps)
fs = 10000  # sampling frequency in Hz

# Function to display the frequency response of a filter
def plot_response(h, fs, title):
    w, H = freqz(h, worN=1024, fs=fs)
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(w, abs(H))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.subplot(1, 2, 2)
    plt.plot(w, 20 * np.log10(abs(H) + 1e-10))
    plt.title('Magnitude in dB')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.ylim(-100, 5)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


cutoff = 3000
h_lp = firwin(N, cutoff, fs=fs) # hamming window is used by default
print("Filter coefficients:") 
print(np.round(h_lp, 4))
plot_response(h_lp, fs, 'FIR Low Pass Filter (Cutoff = 3 kHz)')


cutoff = 3000
h_hp = firwin(N, cutoff, pass_zero=False, fs=fs)
print("Filter coefficients:")
print(np.round(h_hp, 4))
plot_response(h_hp, fs, 'FIR High Pass Filter (Cutoff = 3 kHz)')


# fs = 10 kHz : upper cutoff 6 kHz is above Nyquist (5 kHz), so only 3 kHz is used
h_bp1 = firwin(N, 3000, pass_zero=False, fs=fs)
print("Filter coefficients (fs = 10 kHz):")
print(np.round(h_bp1, 4))
plot_response(h_bp1, fs, 'Band Pass (3-6 kHz), fs = 10 kHz')


# fs = 20 kHz : both cutoffs 3 kHz and 6 kHz are valid
fs2 = 20000
h_bp2 = firwin(N, [3000, 6000], pass_zero=False, fs=fs2)
print("Filter coefficients (fs = 20 kHz):")
print(np.round(h_bp2, 4))
plot_response(h_bp2, fs2, 'FIR Band Pass Filter (3-6 kHz), fs = 20 kHz')


# fs = 10 kHz : upper cutoff 6 kHz is above Nyquist (5 kHz), so only 3 kHz is used 
h_bs1 = firwin(N, 3000, fs=fs)
print("Filter coefficients (fs = 10 kHz):")
print(np.round(h_bs1, 4))
plot_response(h_bs1, fs, 'Band Stop (3-6 kHz), fs = 10 kHz')


# fs = 20 kHz : both cutoffs 3 kHz and 6 kHz are valid fs2 = 20000
h_bs2 = firwin(N, [3000, 6000], fs=fs2) # pass_zero=True gives band stop
print("Filter coefficients (fs = 20 kHz):") 
print(np.round(h_bs2, 4))
plot_response(h_bs2, fs2, 'FIR Band Stop Filter (3-6 kHz), fs = 20 kHz')


