import network
import time
import machine
import requests

WIFI_SSID = "Ziggo3814574"
WIFI_PASSWORD = "kEjbrrbFhxjfptt7"
API_URL = "http://192.168.178.198:8000/temperature"

led = machine.Pin("LED", machine.Pin.OUT)

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
led.on()

while True:
    reading = sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    temperature = round(temperature, 2)

    print("Temperature:", temperature, "°C")
    print("Sending to API...")

    try:
        response = requests.post(
            API_URL,
            json={
                "device_id": "pico-01",
                "temperature": temperature
            }
        )

        print("API status:", response.status_code)
        print("API response:", response.text)

        response.close()

    except Exception as e:
        print("API request failed:", e)

    time.sleep(5)