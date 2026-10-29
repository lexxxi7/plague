import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        if self.verbose:
            print("GPIO cleanup successfully")

    def number_to_dac(self, number):
        bin_str = bin(number)[2:].zfill(8)
        for i in range(8):
            bit_value = int(bin_str[i])
            GPIO.output(self.bits_gpio[i], bit_value)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            comp_value = GPIO.input(self.comp_gpio)
            if self.verbose:
                voltage = (number / 256) * self.dynamic_range
                print(f"Code: {number}, Dac Voltage: {voltage:.2f}V, Comp: {comp_value}")

            if comp_value == 1:
                return number
            
        return 255


    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = (code / 256.0) * self.dynamic_range
        return voltage


if __name__ == '__main__':
    V_REF = 3.3
    adc = None
    try:
        adc = R2R_ADC(dynamic_range=V_REF, verbose=False)

        while True:
            current_voltage = adc.get_sc_voltage()
            print(f"Измеренное напряжение: {current_voltage:.4f} B")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")

    finally:
        if adc is not None:
            del adc
