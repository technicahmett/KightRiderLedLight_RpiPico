from machine import Pin
import utime

leds = [Pin(i) for i in range(1,12)] #to assign pin number for leds. between 1 and 12

for i in range (1,12): # set pin mode to OUT
    Pin(i,Pin.OUT)

while True:
    for n in range (1,11):
        leds[n].on()
        utime.sleep_ms(125)
        leds[n].off()
        print(n)
    
    for n in reversed(range (1,11)):
        leds[n].on()
        utime.sleep_ms(25)
        leds[n].off()
        print(n)
  