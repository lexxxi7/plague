import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title('Зависимость напряжения от времени')
    plt.xlabel('Время')
    plt.ylabel('Напряжения')
    plt.xlim(min(time), max(time))
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time_values):
    sampling_periods = []

    for i in range(len(time_values) - 1):
        delta_t = time_values[i + 1] - time_values[i]
        sampling_periods.append(delta_t)

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=50)
    plt.title('Распределение периодов измерений АЦП')
    plt.xlabel('Период выборки (с)')
    plt.ylabel('Количество измерений')
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()