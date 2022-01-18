import utime
from machine import Pin

led_onboard = Pin(25, Pin.OUT)
led_blue = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)


while True:
    led_blue.toggle()
    utime.sleep_ms(1000)
    print("========")
    print("Sleep")
    print(button.value())
