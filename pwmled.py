from machine import Pin, PWM
import utime

led = PWM(Pin(17))
led.freq(15000)
helligkeit = 0
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        helligkeit = 30000
        led.duty_u16(helligkeit)
        print("led on")
        print(helligkeit)
        
        for x in range(10000, 30000, 10):
            print(helligkeit)
            helligkeit = x
            led.duty_u16(helligkeit)
        else:
            utime.sleep(2)
            led.duty_u16(0)
            print("led off")
        
        
            
  
        
 
