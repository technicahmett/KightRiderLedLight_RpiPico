<h2>How to Make KnightRider Led Light with the RaspberryPi Pico<h2>


<h3>Hi everbody.</h3> 

I have used Raspberry Pico and Micropython in this project. 
You know Pico. Pico is tiny and fast a MCU. But I won't tell you about the Pico. You can find it on the internet If you want...

There are a few titles in this project. I wanted to share these titles when I was learning to MicroPython.
    <p>***I think, Raspbbery Pi Pico will be correct choose if you want to learn MicroPython...***</p>

- Blink led. Led on/off,
- usage the potentiometer,
- usage the TM1637 4 Digit 7 Segment Display,
- usage HC-SR04 Distance sensor,

Finally I put them all together. Of course, I have coded in MicroPython on Thonny IDE.
    
Required equipments:
1. Raspberry Pi Pico,
2. Bargraph LED 10 segments or 10 pcs leds,
3. Potentiometer,
4. TM1637,
5. HC-SR04.

## Connections for Bargraph LED

Rpi Pico    | Bargraph
----------- | -----------
4 (GP2)     | Led1
2 (GP3)     | Led2
6 (GP4)     | Led3
7 (GP5      | Led4
9 (GP6)     | Led5
10 (GP7)    | Led6
11 (GP8)    | Led7
12 (GP9)    | Led8
14 (GP10)   | Led9
15 (GP11)   | Led10
    GND     | GND

<p align="center">
  <img src="https://github.com/technicahmett/KightRiderLeds_RpiPico/blob/main/led_schema.jpg" width="550" title="led schema">
</p>
    
**in the code**
```python
#set pin numbers for LEDs
LEDs = [Pin(i) for i in range(1,12)]

#set pin modes to OUT
for i in range (1,12):
    Pin(i,Pin.OUT)
```
  
## Connections for Potantiometer

Rpi Pico    | POT
----------- | -----------
31 (GP26)   | ADC0 (or)
322 (GP27)  | ADC1 (or)
34 (GP28)   | ADC2 (or)
36 3.3V     | VCC
  (GND)     | GND

<p align="center">
  <img src="https://github.com/technicahmett/KightRiderLeds_RpiPico/blob/main/POT_schema.jpg" width="550" title="Potantiometer schema">
</p>
    
**in the code**
 ```python 
adc = machine.ADC(26)     # add a ADC object on ADC pin
conversion_factor = 200 / (65300) #for maks. 200ms
  ```
      
## Connections for TM1637

Rpi Pico     | TM1637
------------ | ---------------
20 (GP15)    | CLK
19 (GP14)    | DIO
3V3 (or 5V)  | VCC
GND          | GND
    
<p align="center">
  <img src="https://github.com/technicahmett/KightRiderLeds_RpiPico/blob/main/TM1637_schema.jpg" width="550" title="TM1637 schema">
</p>
 
**in the code**
 ```python  
#set tm1637 LCD 
tm = tm1637.TM1637(clk=Pin(15), dio=Pin(14))
   ```
  
  
## Connections for HC-SR04

Rpi Pico    | HC-SR04
----------- | ---------------
22 (GP17)   | Trigger Pin
21 (GP16)   | Echo Pin
40  (5V)    | VCC
GND         | GND
  
<p align="center">
  <img src="https://github.com/technicahmett/KightRiderLeds_RpiPico/blob/main/HCSR04_schema.jpg" width="550" title="HCSR04 schema">
</p>
 
**in the code**
  ```python
# set pin number for HCSR04
sensor = HCSR04(trigger_pin=17, echo_pin=16)
```
  
   

## Special Thanks
* [For tm1637 library file](https://github.com/mcauser/micropython-tm1637)
* [For hc-sr04 library file](https://github.com/rsc1975/micropython-hcsr04)
* [HC-SR04 Wiki](https://www.mpja.com/download/hc-sr04_ultrasonic_module_user_guidejohn.pdf)
* [TM1637 Wiki](https://github.com/Seeed-Studio/Grove_4Digital_Display)
  
 ## Links

* [Raspbbery Pi Pico Getting started](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
* [MicroPython Pi Documents](https://docs.micropython.org/en/latest/rp2/quickref.html)
* [RPi_PiPico_Digital_v10-pdf](https://hackspace.raspberrypi.com/books/micropython-pico/)
* [Getting started with Raspberry Pi Pico-pdf](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
* [Thonny IDE](https://thonny.org)

  
  ***Don't forget the Star...***
