# Unit Impusle

import numpy as np
import matplotlib.pyplot as plt

def unit_impulse(length, position):
    signal = np.zeros(length)
    signal[position] = 1
    return signal

start, stop, step = -10, 10, 1
x = np.arange(start, stop + step, step)

signal1 = unit_impulse(len(x), abs(start)//step)

plt.stem(x, signal1)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('unit impulse signal')
plt.grid(True)
plt.show()



# --------------------------------------------------------------------------------------------------

# inmpulse Function

import numpy as np
import matplotlib.pyplot as plt

def impulse(signal_length, period):
    impulse1 = np.zeros(signal_length)
    for n in range(signal_length):
        if n % period == 0:
            impulse1[n] = 1
    return impulse1

signal_length = 100
period = 10

impulse_signal = impulse(signal_length, period)

plt.stem(impulse_signal)
plt.title('Impulse Train')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

# -----------------------------------------

# Continous and Discrete 
import numpy as np
import matplotlib.pyplot as plt

def continuous(time):
    unit_step = np.zeros_like(time)
    unit_step[time >= 0] = 1
    return unit_step

def discrete(samples):
    unit_step = np.zeros(samples)
    unit_step[samples // 2:] = 1
    return unit_step

time = np.linspace(-5, 5, 1000)
continuous_unit_step = continuous(time)

samples = 20
discrete_unit_step = discrete(samples)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_unit_step)
plt.title('continuous unit step signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2, 1, 2)
plt.stem(discrete_unit_step)
plt.title('discrete unit step signal')
plt.xlabel('sample')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()

# --------------------------------------

#Ramp Signal

import numpy as np
import matplotlib.pyplot as plt

def continuous(time, slope):
    ramp = np.zeros_like(time)
    ramp[time >= 0] = slope * time[time >= 0]
    return ramp

def discrete(samples, slope):
    ramp = np.zeros(samples)
    ramp[samples // 2:] = slope * np.arange(samples // 2, samples)
    return ramp

time = np.linspace(-5, 5, 1000)
samples = 20
slope = 2

continuous_ramp = continuous(time, slope)
discrete_ramp = discrete(samples, slope)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_ramp)
plt.title('continuous ramp signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2, 1, 2)
plt.stem(discrete_ramp)
plt.title('discrete ramp signal')
plt.xlabel('sample')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()

# ----------------------------------------------------

# Exponential 

import numpy as np
import matplotlib.pyplot as plt

def continuous(time, amplitude, coefficient):
    return amplitude * np.exp(coefficient * time)

def discrete(samples, amplitude, coefficient):
    return amplitude * np.exp(coefficient * np.arange(samples))

time = np.linspace(0, 5, 1000)
samples = 20
amplitude = 2
coefficient = -0.5

continuous_exponential = continuous(time, amplitude, coefficient)
discrete_exponential = discrete(samples, amplitude, coefficient)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_exponential)
plt.title('continuous exponential signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2, 1, 2)
plt.stem(discrete_exponential)
plt.title('discrete exponential signal')
plt.xlabel('sample')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------------------------------------
# Parabolic
import numpy as np
import matplotlib.pyplot as plt

def continuous(time, coefficients):
    return np.polyval(coefficients, time)

def discrete(samples, coefficients):
    return np.polyval(coefficients, np.arange(samples))

time = np.linspace(-5, 5, 1000)
samples = 20
coefficients = [1, 2, 1]

continuous_parabolic = continuous(time, coefficients)
discrete_parabolic = discrete(samples, coefficients)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_parabolic)
plt.title('continuous parabolic signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2, 1, 2)
plt.stem(discrete_parabolic)
plt.title('discrete parabolic signal')
plt.xlabel('sample')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()

#---------------------------------------------------------------------------------------------------
# Sine Way continous and Discreate

import numpy as np
import matplotlib.pyplot as plt

def continuous(time, amplitude, frequency, phase):
    return amplitude * np.sin(2 * np.pi * frequency * time + phase)

def discrete(samples, sampling_frequency, amplitude, frequency, phase):
    time = np.arange(samples) / sampling_frequency
    return amplitude * np.sin(2 * np.pi * frequency * time + phase)

time = np.linspace(0, 1, 1000)
samples = 100
sampling_frequency = 10
amplitude = 1
frequency = 2
phase = 0

continuous_sine_wave = continuous(time, amplitude, frequency, phase)
discrete_sine_wave = discrete(samples, sampling_frequency, amplitude, frequency, phase)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, continuous_sine_wave)
plt.title('continuous sine wave signal')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2, 1, 2)
plt.stem(discrete_sine_wave)
plt.title('discrete sine wave signal')
plt.xlabel('sample')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()
#-----------------------------------------------------------------------------------------------------
# Output Signal

import numpy as np
import matplotlib.pyplot as plt

def unit(x):
    return np.where(x >= 0, 1, 0)

axis = np.linspace(-10, 10, 1000)

output_signal = unit(axis) + unit(axis - 1) + 3 * unit(axis + 5)

plt.plot(axis, output_signal)
plt.title('y(t) = u(t) + u(t-1) + 3u(t+5)')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.ylim([-0.5, 5.5])
plt.grid(True)
plt.show()

# -------------------------------------------------------------------------------------------------------------------
# Unit 

import numpy as np
import matplotlib.pyplot as plt

def unit(x, val):
    result = np.zeros(len(x))
    result[x == val] = 1
    return result

n_axis = np.arange(-10, 11)

signal = unit(n_axis, 0) + unit(n_axis, 1) + 3 * unit(n_axis, -5)

plt.stem(n_axis, signal)
plt.title('y(t) = delta(t) + delta(t-1) + 3delta(t+5)')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.ylim([-0.5, 4.5])
plt.grid(True)
plt.show()