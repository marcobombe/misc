import time
import board
from digitalio import DigitalInOut, Direction

pad_pin = board.D17

pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

already_pressed = False
count = 0
while True:

    if pad.value and not already_pressed:
        count = count + 1
        print("pressed " + str(count))


    already_pressed = pad.value
    time.sleep(0.1)
