import neopixel
import board
import time
from adafruit_circuitplayground import cp

A2= neopixel.NeoPixel(
    board.A2, 30, brightness=0.1, auto_write=False)

A5= neopixel.NeoPixel(
    board.A5, 30, brightness=0.1, auto_write=False)

while True:
    A2.fill((255,0,0))
    A5.fill((255,0,0))
    A2.show()
    A5.show()
    time.sleep(0.25)

    if cp.touch_A7:
        for n in range(5):
            A5.fill((0,0,0))
            A5.show()
            time.sleep(0.25)
            A5.fill((225,0,0))
            A5.show()
            time.sleep(0.25)
    if cp.touch_A1:
        for n in range(5):
            A2.fill((0,0,0))
            A2.show()
            time.sleep(0.25)
            A2.fill((225,0,0))
            A2.show()
            time.sleep(0.25)
    else:
        continue
