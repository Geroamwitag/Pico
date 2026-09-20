import network
import time
import machine

WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

sensor = machine.ADC(4)
conversion_factor = 3.3 / 65535

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting to Wi-Fi...")

wlan.connect(WIFI_SSID, WIFI_PASSWORD)

while not wlan.isconnected():
    print(".", end="")
    time.sleep(1)

print()
print("Connected!")
print("IP address:", wlan.ifconfig()[0])

while True:
    reading = sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721

    print("Temperature:", round(temperature, 2), "°C")

    time.sleep(2)