import numpy
import time

def get_sin_wave_amplitude(freq, time_val):
    raw_sin = numpy.sin(2 * numpy.pi * freq * time_val)
    norm_sin = (raw_sin + 1) / 2
    return norm_sin

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)

def get_triangle_wave_amplitude(freq, time_val):
    period = 1.0 / freq
    phase = (time_val % period) / period
    if phase < 0.5: return 2.0 * phase
    else: return 2.0 * (1.0 - phase)
