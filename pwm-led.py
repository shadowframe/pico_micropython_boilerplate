from machine import Pin, PWM
import utime

#led = PWM(Pin(17))
led = Pin(17, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)
        print("led on")
        utime.sleep(2)
        led.value(0)
        print("led off")

# from machine import Pin, PWM
# import utime
#
# led = PWM(Pin(17))
# led.freq(1000)
# led.duty_u16(2000)
#
# button = Pin(16, Pin.IN, Pin.PULL_DOWN)
#
# while True:
#     if button.value() == 1:
#         led.duty_u16(3000)
#         utime.sleep(3)


