import lcd160cr
import pyb
import time
import random

lcd= lcd160cr.LCD160CR('X')
time.sleep(2)
lcd.erase()

#CREATE VARIABLE FOR LIGHTS RANGE(1,5)
"""
red= pyb.LED(1)
green= pyb.LED(2)
yellow = pyb.LED(3)
blue = pyb.LED(4)
"""

#INTERACT WITH ALL LIGHTS
"""
leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
    l.off()

n = 0
try:
   while True:
      n = (n + 1) % 4
      leds[n].toggle()
      pyb.delay(50)
finally:
    for l in leds:
        l.off()


#SET SENSITIVITY FOR LIGHT ON / OFF

accel = pyb.Accel()
yellow = pyb.LED(3)
SENSITIVITY = 10

while True:
    x = accel.x()
    if abs(x) > SENSITIVITY:
        yellow.on()
    else:
        yellow.off()

    pyb.delay(100)while 
"""
#WACK A MOLE


"""
lcd.set_pos(50, 50)
lcd.write('WACK A MOLE')
time.sleep(2)
lcd.erase()
#lcd.set_pos(50, 50)
lcd.write('START IN...')
time.sleep(2)
lcd.erase()
#lcd.set_pos(50, 50)
lcd.write('3...')
time.sleep(1)
lcd.erase()
#lcd.set_pos(50, 50)
lcd.write('2...')
time.sleep(1)
lcd.erase()
#lcd.set_pos(50, 50)
lcd.write('1...')
time.sleep(1)
lcd.erase()
#lcd.set_pos(50, 50)
lcd.write('GO...')
time.sleep(1)
lcd.erase()
"""
"""
while True:
	[t,x,y]=lcd.get_touch()
	str_line='%d %d %d' %(t,x,y)
	lcd.set_pos(50, 50)
	lcd.write(str_line)
	n=random.randint(1,4)
	pyb.LED(n).on()
	lcd.set_pos(50, 80)
	lcd.write(colours[n])
	time.sleep(2)
	pyb.LED(n).off()
	lcd.erase()

"""
#DRAW LINES
"""
for each colour, y must be...
blue smaller than 39
yellow smaller than 78
green smaller than 115
else red
"""
#DRAW RECTANGLES

blue=lcd.rgb(0,0,255)
yellow=lcd.rgb(255,255,0)
green=lcd.rgb(0,255,0)
red=lcd.rgb(255,0,0)
black=lcd.rgb(0,0,0)
white=lcd.rgb(255,255,255)
"""
lcd.set_pen(blue,blue)
lcd.rect(0,0,150,40)
lcd.set_pen(yellow,yellow)
lcd.rect(0,41,150,40)
lcd.set_pen(green,green)
lcd.rect(0,81,150,40)
lcd.set_pen(red,red)
lcd.rect(0,121,150,40)
"""
colours={1:'red',2:'green',3:'yellow',4:'blue'}
col={'blue':[0,int(((lcd.h)/4)*1)],'yellow':[int(((lcd.h)/4)*1)+1,int(((lcd.h)/4)*2)],'green':[int(((lcd.h)/4)*2)+1,int(((lcd.h)/4)*3)],'red':[int(((lcd.h)/4)*3)+1,int(((lcd.h)/4)*4)]}

score=[]
s=0
lcd.set_font(3,scroll=1)
while s<10:
	s=s+1
	lcd.erase()
	lcd.set_pen(blue,blue)
	lcd.rect(0,0,lcd.w,int((lcd.h)/4))
	lcd.set_pen(yellow,yellow)
	lcd.rect(0,int((((lcd.h)/4)*1)+1),lcd.w,int((lcd.h)/4))
	lcd.set_pen(green,green)
	lcd.rect(0,int((((lcd.h)/4)*2)+1),lcd.w,int((lcd.h)/4))
	lcd.set_pen(red,red)
	lcd.rect(0,int((((lcd.h)/4)*3)+1),lcd.w,int((lcd.h)/4))
	
	n=random.randint(1,4)
	pyb.LED(n).on()
	time.sleep(1)
	pyb.LED(n).off()

	lcd.set_pen(white,white)
	[t,x,y]=lcd.get_touch()
	
	if col[colours[n]][0]<y<col[colours[n]][1]:
		lcd.set_pos(x,y)
		lcd.write(colours[n])
		time.sleep(2)
		score.append(1)	
	else:
		lcd.set_pos(x,y)
		lcd.write('0')
		score.append(0)
		time.sleep(2)


lcd.set_pos(20,50)
message='final score:'
result=str(int((sum(score)/len(score))*100))
lcd.write(message)
lcd.set_pos(50,80)
lcd.write(result)


