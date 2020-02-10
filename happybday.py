import random
import pyb
import time
import lcd160cr


lcd= lcd160cr.LCD160CR('X')
lcd.erase()

pyb.delay(2000)

blue=lcd.rgb(0,0,255)
yellow=lcd.rgb(255,255,0)
green=lcd.rgb(0,255,0)
red=lcd.rgb(255,0,0)
black=lcd.rgb(0,0,0)
white=lcd.rgb(255,255,255)


accel = pyb.Accel()

coords=[]

for n in range(10,30):
	coords.append((10,n))#M
	coords.append((20,n))#M
	coords.append((35,n))#A
	coords.append((45,n))#A
	coords.append((60,n))#R
	coords.append((90,n))#I
	coords.append((110,n))#E

for n in range(10,20):
	coords.append((70,n))#R

for n in range(1,10):
	coords.append((35+n,10))#A
	coords.append((35+n,20))#A
	coords.append((110+n,10))#E
	coords.append((110+n,20))#E
	coords.append((110+n,30))#E
	coords.append((60+n,10))#R
	coords.append((60+n,20))#R


for n in range(1,5):
	coords.append((10+n,10+n))#M
	coords.append((15+n,15-n))#M

for n in range(1,10):
	coords.append((60+n,20+n))#R

while len(coords)>0:
	light=random.randint(1,4)
	pyb.LED(light).toggle()

	colour=lcd.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	lcd.set_pen(colour,colour)
	x=random.choice(coords)
	lcd.dot(x[0],x[1])
	coords.remove(x)
	pyb.delay(50)


pyb.delay(1000)

lcd.set_font(3,scroll=1)
lcd.set_pos(40,50)
lcd.write('TURN ME')
lcd.set_pos(40,70)
lcd.write('OVER')

while True:
	x,y,z =accel.x(), accel.y(), accel.z()
	if z>0:
		pass
	else:
		lcd.erase()
		lcd.set_pos(40,50)
		lcd.write('HAPPY')
		lcd.set_pos(40,70)
		lcd.write('BIRTHDAY')
		break

while True:
	light=random.randint(1,4)
	pyb.LED(light).toggle()
	pyb.delay(50)



