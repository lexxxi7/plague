import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 2.0
signal_frequency = 20
sampling_frequency = 500

try:
    dac = mcp.MCP4725(5.2, 0x61)
    while True:
        current_time = time.time()
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        target_voltage = norm_amp * amplitude
        dac.set_voltage(target_voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    print("\nbebebe")
finally:
    if 'dac' in locals():
        dac.deinit()