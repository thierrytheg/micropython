import random
import pyb
import time
import lcd160cr


lcd= lcd160cr.LCD160CR('X')
lcd.erase()

pyb.delay(2000)

while True:
	a,b,c=lcd.get_touch()
	x=random.randint(0,lcd.w)
	y=random.randint(0,lcd.h)
	colour=lcd.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	if a==0:	
		lcd.set_pen(colour,colour)
		lcd.dot(x,y)
	else:
		lcd.erase()
		continue
