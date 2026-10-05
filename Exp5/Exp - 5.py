import numpy as np
import matplotlib.pyplot as plt

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Calculate FFT
fft_result = np.fft.fft(signal)
print(fft_result)

# Calculate Magnitude Spectrum
magnitude_spectrum = np.abs(fft_result)
print(magnitude_spectrum)

# Calculate Phase Spectrum
phase_spectrum = np.angle(fft_result)
print(phase_spectrum)

# Reconstruct the original signal using IFFT
reconstructed_signal = np.fft.ifft(fft_result)
print(reconstructed_signal)

sample_index = np.arange(len(signal))

plt.figure(figsize=(12, 10))

# Plot 1: Original Signal
plt.subplot(2, 2, 1)
plt.stem(sample_index, signal)
plt.title('Original Signal')
plt.xlabel('Frequency Index')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot 2: Magnitude Spectrum
plt.subplot(2, 2, 2)
plt.stem(sample_index, magnitude_spectrum)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude Spectrum')
plt.grid(True)

# Plot 3: Phase Spectrum
plt.subplot(2, 2, 3)
plt.stem(sample_index, phase_spectrum)
plt.title('Phase Spectrum')
plt.xlabel('Frequency Index')
plt.ylabel('Phase Spectrum')
plt.grid(True)

# Plot 4: Reconstructed Signal
plt.subplot(2, 2, 4)
plt.stem(sample_index, reconstructed_signal)
plt.title('Reconstructed Signal')
plt.xlabel('Frequency Index')
plt.ylabel('Reconstructed Signal')
plt.grid(True)

plt.tight_layout()
plt.show()