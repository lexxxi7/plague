from mcp3021_driver import MCP3021
import time

import matplotlib.pyplot as plt

if __name__ == "__main__":
    measured_dynamic_range = 5.0
    device = MCP3021(dynamic_range=measured_dynamic_range)
    voltages = []
    times = []
    duration = 15
    try:
        start_time = time.time()
        while time.time() - start_time < duration:
            current_elapsed = time.time() - start_time
            current_voltage = device.get_voltage()
            voltages.append(current_voltage)
            times.append(current_elapsed)
            time.sleep(0.1)
        print('stop')
        plt.figure(figsize=(10, 5))
        plt.plot(times, voltages)
        plt.xlabel('Время от начала эксперимента')
        plt.ylabel('Напряжение')
        plt.grid(True)
        plt.legend()

        plt.figure(figsize=(9, 5))
        plt.hist(voltages, bins=15)
        plt.xlabel('Напряжение')
        plt.ylabel('Количество отсчетов')
        plt.grid(True)
        plt.legend()

        plt.show()
    
    finally:
        if device is not None:
            device.deinit()