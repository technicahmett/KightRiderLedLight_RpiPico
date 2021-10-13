from machine import Pin
import utime

leds = [Pin(i) for i in range(1,12)] #to assign pin number for leds. between 1 and 12

for i in range (1,12): # set pin mode to OUT
    Pin(i,Pin.OUT)

"""
led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)
led5 = Pin(6, Pin.OUT)
led6 = Pin(7, Pin.OUT)
led7 = Pin(8, Pin.OUT)
led8 = Pin(9, Pin.OUT)
led9 = Pin(10, Pin.OUT)
led10 = Pin(11, Pin.OUT)
"""

while True:
    for n in range (1,11):
        leds[n].on()
        utime.sleep_ms(100)
        leds[n].off()
    """
    led1.value(1)
    utime.sleep_ms(100)
    led1.value(0)
    led2.value(1)
    utime.sleep_ms(100)
    led2.value(0)
    led3.value(1)
    utime.sleep_ms(100)
    led3.value(0)
    led4.value(1)
    utime.sleep_ms(100)
    led4.value(0)
    led5.value(1)
    utime.sleep_ms(100)
    led5.value(0)
    led6.value(1)
    utime.sleep_ms(100)
    led6.value(0)
    led7.value(1)
    utime.sleep_ms(100)
    led7.value(0)
    led8.value(1)
    utime.sleep_ms(100)
    led8.value(0)
    led9.value(1)
    utime.sleep_ms(100)
    led9.value(0)
    led10.value(1)
    utime.sleep_ms(100)
    led10.value(0)
"""
    