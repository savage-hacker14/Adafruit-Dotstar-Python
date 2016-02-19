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
datapin   = 23
clockpin  = 24
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

delay = 2.0 / 256.0

while True:                              # Loop forever
        
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

                for i in range(31):             #Step through all pixels in my led strip (1-30)
#                        strip.setPixelColor(i, color) # Turn on pixel #i
                        strip.setPixelColor(i, color + i / 32 * 0xFF) # Turn on pixel #i

                strip.show()                     # Refresh strip

                time.sleep(delay)            # pause delay seconds

        
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

                for i in range(31):             #Step through all pixels in my led strip (1-30)
                        strip.setPixelColor(i, color) # Turn on pixel #i
                strip.show()                     # Refresh strip

                time.sleep(delay)            # Pause 20 milliseconds (~50 fps)
        
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

                for i in range(31):             #Step through all pixels in my led strip (1-30)
                        strip.setPixelColor(i, color) # Turn on pixel #i
                strip.show()                     # Refresh strip

                time.sleep(delay)            # Pause 20 milliseconds (~50 fps)


