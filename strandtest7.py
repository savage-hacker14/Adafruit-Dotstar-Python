#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
from dotstar import Adafruit_DotStar

numpixels = 30 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin   = 16
clockpin  = 12
#strip     = Adafruit_DotStar(numpixels, datapin, clockpin)
strip     = Adafruit_DotStar(numpixels, datapin, clockpin,order='bgr')

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.
# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)

strip.begin()           # Initialize pins for output
strip.setBrightness(32) # Limit brightness to ~1/4 duty cycle

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

delay = 5.5 / 256.0
head = 0

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import time
import RPi.GPIO as GPIO

lcd = Adafruit_CharLCD()

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(16, 1)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while True:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        lcd.message(' Banpo Bridge \n')
        lcd.message(' By Jay and Jake')
        time.sleep(3)

        
        #------------------#
        # Red -> Green
        #------------------#
        
        r_start = 0xFF
        g_start = 0x00
        b_start = 0x00

        for s in range(0x00,0xFF):
                r = r_start - s
                g = g_start + s
                b = b_start
                
                color = r*0x010000 + g*0x000100 + b*0x000001
                time.sleep(delay)
                head += 1

                for i in range(31):             #Step through all pixels in my led strip (1-30)
#                        strip.setPixelColor(i, color) # Turn on pixel #i
                        strip.setPixelColor(i, color + i * 0xFF / 32 + s + head) # Turn on pixel #i

                strip.show()                     # Refresh strip

                time.sleep(delay)            # pause delay seconds
                head += 1
        
        #------------------#
        # Green -> Blue
        #------------------#
         
        r_start = 0x00
        g_start = 0xFF
        b_start = 0x00

        for s in range(0x00,0xFF):
                r = r_start 
                g = g_start - s 
                b = b_start + s
                
                color = r*0x010000 + g*0x000100 + b*0x000001
                time.sleep(delay)
                head += 1

                for i in range(31):             #Step through all pixels in my led strip (1-30)
#                        strip.setPixelColor(i, color) # Turn on pixel #i
                        strip.setPixelColor(i, color + i * 0xFF / 32 + s + head) # Turn on pixel #i

                strip.show()                     # Refresh strip

                time.sleep(delay)            # pause delay seconds
                head += 1
        
        #------------------#
        # Blue -> Red
        #------------------#
         
        r_start = 0x00
        g_start = 0x00
        b_start = 0xFF

        for s in range(0x00,0xFF):
                r = r_start + s
                g = g_start
                b = b_start - s
                
                color = r*0x010000 + g*0x000100 + b*0x000001
                time.sleep(delay)
                head += 1

                for i in range(31):             #Step through all pixels in my led strip (1-30)
#                        strip.setPixelColor(i, color) # Turn on pixel #i
                        strip.setPixelColor(i, color + i * 0xFF / 32 + s + head) # Turn on pixel #i

                strip.show()                     # Refresh strip

                time.sleep(delay)            # pause delay seconds
                head += 1
except KeyboardInterrupt:
        pass
    
r_start.stop()
g_start.stop()
b_start.stop()


