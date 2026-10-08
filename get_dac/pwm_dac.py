import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

        if self.verbose:
            print(f"ШИМ ЦАП инициализирован на пине {self.gpio_pin} с частотой {self.pwm_frequency} Гц")

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()
        if self.verbose:
            print("Работа ШИМ ЦАП завершена, ресурсы GPIO очищены")
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение {voltage} В вышло за динамический диапазон (0.0 - {self.dynamic_range} В)")
            return

        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.3f} В (коэффициент заполнения: {duty_cycle:.1f}%)")


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.296, True)

        while True:
            try:
                voltage = float(input("ВВедите напряжение в вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()