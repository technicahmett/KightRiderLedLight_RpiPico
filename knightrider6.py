from machine import Pin
import utime
import machine
import tm1637
from hcsr04 import HCSR04

tm = tm1637.TM1637(clk=Pin(15), dio=Pin(14)) #set tm1637 LCD

#all LEDs off for clean
tm.write([0, 0, 0, 0])
tm.show('    ')

leds = [Pin(i) for i in range(1,12)] #to assign pin number for leds. between 1 and 12

for i in range (1,12): # set pin mode to OUT
    Pin(i,Pin.OUT)

sensor = HCSR04(trigger_pin=17, echo_pin=16)

while True:
    speed = int(sensor.distance_cm())
    for n in range (1,11):
        leds[n].on()
        utime.sleep_ms(speed)
        leds[n].off()
        print(speed)
    
    for n in reversed(range (1,11)):
        leds[n].on()
        utime.sleep_ms(speed)
        leds[n].off()
        print(speed)
    tm.number(speed)