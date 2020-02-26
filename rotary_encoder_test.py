from RPi import GPIO
from time import sleep

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

clk = 17
dt = 18
sw = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
debounce_counter = 0
clkLastState = GPIO.input(clk)
try:
        while True:
                clkState = GPIO.input(clk)
                if clkState != clkLastState:
                        dtState = GPIO.input(dt)
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                clkLastState = clkState
                
                if GPIO.input(sw) == GPIO.LOW:
                        debounce_counter += 1
                if debounce_counter == 25:        
                        print("Button was pushed!")
                        debounce_counter = 0
                
                sleep(0.01)
finally:
        GPIO.cleanup()
