import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.3
signal_frequency = 10
sampling_frequency = 1000
try:
    dac = pwm.PWM_DAC(12, 500, 3.3)
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