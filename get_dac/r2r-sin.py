import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 2.0
signal_frequency = 20
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2)

    while True:
        current_time = time.time()             
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        target_voltage = norm_amp * amplitude
        dac.set_voltage(target_voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    print("\nОстановка генерации пользователем")

finally:
    if 'dac' in locals():
        dac.deinit()
