from machine import Pin
import utime

leds = [Pin(i) for i in range(1,12)] #to assign pin number for leds. between 1 and 12

for i in range (1,12): # set pin mode to OUT
    Pin(i,Pin.OUT)

adc = machine.ADC(27) #add a potentiometer on ADC pin
conversion_factor = 200 / (65300)

while True:
    speed = int(adc.read_u16()*conversion_factor)
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
  