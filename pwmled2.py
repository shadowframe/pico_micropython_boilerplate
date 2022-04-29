from machine import Pin, PWM
import time as time

led = PWM(Pin(17))
led.freq(15000)
duty = 100
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led.duty_u16(duty)

while True:
    led.duty_u16(duty)
    if button.value() == 1:
        duty = 5
        while True:
          duty = duty + 1000
          led.duty_u16(duty) 
          time.sleep(0.05)
          print(duty)
          if duty > 60000:
            duty = 0
            break

