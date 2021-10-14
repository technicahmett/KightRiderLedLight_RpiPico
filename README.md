# KightRiderLeds_RpiPico
<h2>Make Knight Rider Led with the RaspberryPi Pico<h2>


<h3>Hi everbody.</h3> 

I have used Raspberry Pico and Micropython in this project. 
You know Pico. Pico is tiny and fast a MCU. But I won't tell you the Pico. You can find on internet If you want.

There are a few titles in this project. I wanted to share these titles when I was learning to MicroPython.
***I think, Raspbbery Pi Pico will be correct choose if you want to learn MicroPython...***

- Blink led. Led on/off,
- use the potentiometer,
- use the TM1637 4 Digit 7 Segment Display,
- use HC-SR04 Distance sensor,

Finally I put them all together. Of course, I made coded using MicroPython on Thonny IDE.

Required equipments:
1. Raspberry Pi Pico
2. Bargraph LED 10 segments or 10 pcs leds.
3. Potentiometer
4. TM1637
5. HC-SR04 

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

**Basic usage**

```python
#set pin numbers for LEDs
LEDs = [Pin(i) for i in range(1,12)]

#set pin modes to OUT
for i in range (1,12):
    Pin(i,Pin.OUT)
```
  
    
## Connections for TM1637

Rpi Pico     | TM1637
------------ | ---------------
20 (GP15)    | CLK
19 (GP14)    | DIO
3V3 (or 5V)  | VCC
GND          | GND
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
