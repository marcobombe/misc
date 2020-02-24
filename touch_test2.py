import time
import board
from digitalio import DigitalInOut, Direction

pad_pin = board.D17

pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT
counter = 0
while True:

    if pad.value:
        counter = counter + 1
        print("pressed" + str(counter))
        
    time.sleep(0.3)
