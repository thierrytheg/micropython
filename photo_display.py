import lcd160cr
import pyb
import time
import random
import os


lcd= lcd160cr.LCD160CR('X')
lcd.erase()

os.chdir(r'/sd/pictures')

while True:
	x=random.randint(0,(len(os.listdir(os.getcwd())))-1)
	pic=os.listdir()[x]
	handle=open(pic,'rb').read()
	lcd.set_pos(0, 0)	
	lcd.jpeg(handle)
	pyb.delay(2000)
	lcd.erase()
