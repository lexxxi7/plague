import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

max_voltage = 3.3
adc = R2R_ADC(dynamic_range=max_voltage, compare_time=0.0001)
voltage_values = []
time_values = []
duration = 3.0
try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        current_elapsed = time.time() - start_time
        current_voltage = adc.get_sar_voltage()
        voltage_values.append(current_voltage)
        time_values.append(current_elapsed)

    plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    plot_sampling_period_hist(time_values)

finally:
    if 'adc' in locals():
        adc.deinit()