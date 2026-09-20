import machine
import time

sensor = machine.ADC(4)
conversion_factor = 3.3 / 65535

while True:
    reading = sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721

    print("Temperature:", round(temperature, 2), "°C")

    time.sleep(2)