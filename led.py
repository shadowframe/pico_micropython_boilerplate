from machine import Pin
import utime

led = Pin(17, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)
        print("led on")
        utime.sleep(2)
        led.value(0)
        print("led off")
