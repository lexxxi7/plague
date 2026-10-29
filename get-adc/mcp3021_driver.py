import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number

    def get_voltage(self):
        raw_value = self.get_number()
        depth = 10
        max_cells = (1 << depth) - 1
        voltage = (raw_value * self.dynamic_range) / max_cells
        return voltage

if __name__ == "__main__":
    measured_dynamic_range = 5.0
    device = None
    try:
        device = MCP3021(dynamic_range=measured_dynamic_range)
        while True:
            current_voltage = device.get_voltage()
            print(f"{current_voltage:.3f}")
            time.sleep(1)

    except KeyboardInterrupt:
        print('lalala')
    finally:
        if device is not None:
            device.deinit()