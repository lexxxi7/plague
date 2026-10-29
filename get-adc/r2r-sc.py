import time
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist
from r2r_adc import R2R_ADC

adc = R2R_ADC(dynamic_range=3.3, compare_time=0.0001)
max_voltage = 3.3
voltage_values = []
time_values = []
duration = 3.0
try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        current_elapsed = time.time() - start_time
        digital_code = adc.sequential_counting_adc()
        current_voltage = (digital_code / 256) * max_voltage
        voltage_values.append(current_voltage)
        time_values.append(current_elapsed)

    plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    plot_sampling_period_hist(time_values)

finally:
    if 'adc' in locals():
        adc.deinit()


