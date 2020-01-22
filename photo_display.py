import lcd160cr
import machine
import time
import random
import os
import sys
import pyb

lcd= lcd160cr.LCD160CR('X')
lcd.erase()

os.chdir(r'/sd/pictures')

while True:
	try:
		x=random.randint(0,(len(os.listdir(os.getcwd())))-1)
		pic=os.listdir()[x]
		print(x)
		handle=open(pic,'rb').read()
		lcd.set_pos(0, 0)	
		lcd.jpeg(handle)
		pyb.delay(2000)
		lcd.erase()

	except:
		continue
		
