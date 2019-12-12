import pyautogui
import numpy



#INSTRUCCIONES UTILES
#########################################
#pyautogui.moveTo(x, y, duration=1)
#		 # current mouse x and y
#pyautogui.size()  # current screen resolution width and height
################################################################


pyautogui.click(140, 860, clicks=1, interval=0, button='left')
pyautogui.click(120, 15, clicks=1, interval=0, button='left')
start = pyautogui.locateOnScreen('start.png')
startx, starty = pyautogui.center(start)
pyautogui.click(startx, starty, clicks=1, interval=0, button='left')
pyautogui.click(852, 390,)
pyautogui.click(852, 502,)
#pyautogui.click(740, 390,)

tablero=numpy.array([-1]*64)
tablero = numpy.reshape(tablero,(8,8))
x=735
y=390
def grafer():
	x=735
	y=390
	for j in range(8):
		for i in range(8):
			#pyautogui.moveTo(x,y)
			
			if (pyautogui.locateOnScreen('0.png', grayscale=True,region=(x,y, 16, 16))) is not None:
				tablero[j,i]=0
			elif (pyautogui.locateOnScreen('1.png',grayscale=True, region=(x,y, 16, 16))) is not None:
				tablero[j,i]=1
			elif (pyautogui.locateOnScreen('2.png',grayscale=True, region=(x,y, 16, 16))) is not None:
				tablero[j,i]=2
			elif (pyautogui.locateOnScreen('3.png',grayscale=True, region=(x,y, 16, 16))) is not None:
				tablero[j,i]=3
			elif (pyautogui.locateOnScreen('4.png',grayscale=True, region=(x,y, 16, 16))) is not None:
				tablero[j,i]=4
			elif (pyautogui.locateOnScreen('mina.png',grayscale=True, region=(x,y, 16, 16))) is not None:
				tablero[j,i]=-2
			x+=16
		x=735
		y+=16
grafer()

x=740
y=400
for j in range(6):
	for i in range(6):
		t=tablero[i:i+3,j:j+3]
		if t[0,0]>=0 and t[0,1]>=0 and t[0,2]>=0 and t[1,0]>=0 and t[1,1]==1 and t[1,2]>=0 and t[2,0]==-1 and t[2,1]>=0 and t[2,2]>=0:
			pyautogui.moveTo(x+j*16, y+(i+2)*16, duration=1)
			pyautogui.click(x+j*16, y+(i+2)*16 , clicks=1, interval=0, button='right')
			tablero[i+2,j]=-2

			print("win")

		elif t[0,0]>=0 and t[0,1]>=0 and t[0,2]>=0 and t[1,0]>=0 and t[1,1]==1 and t[1,2]>=0 and t[2,0]>=0 and t[2,1]>=0 and t[2,2]==-1:
			pyautogui.moveTo(x+(j+2)*16, y+(i+2)*16, duration=1)
			pyautogui.click(x+(j+2)*16, y+(i+2)*16 , clicks=1, interval=0, button='right')
			tablero[i,j+2]=-2
			print("win2")

		elif t[0,0]==-1 and t[0,1]>=0 and t[0,2]>=0 and t[1,0]>=0 and t[1,1]==1 and t[1,2]>=0 and t[2,0]>=0 and t[2,1]>=0 and t[2,2]>=0:
			pyautogui.moveTo(x+j*16, y+i*16, duration=1)
			pyautogui.click(x+j*16, y+i*16 , clicks=1, interval=0, button='right')
			tablero[i,j]=-2
			print("win3")
			

		elif t[0,0]>=0 and t[0,1]>=0 and t[0,2]==-1 and t[1,0]>=0 and t[1,1]==1 and t[1,2]>=0 and t[2,0]>=0 and t[2,1]>=0 and t[2,2]>=0:
			pyautogui.moveTo(x+(j+2)*16, y+i*16, duration=1)
			pyautogui.click(x+(j+2)*16, y+i*16 , clicks=1, interval=0, button='right')
			tablero[i+2,j+2]=-2
			print("win4")
x=740
y=400
for j in range(6):
	for i in range(6):
		t=tablero[i:i+3,j:j+3]
		if t[1,1]==1 and (t[0,0]==-2 or t[0,1]==-2 or t[0,2]==-2 or t[1,0]==-2  or t[1,2]==-2 or t[2,0]==-2 or t[2,1]==-2 or t[2,2]==-2) :
			for jj in range(2):
				for ii in range(2):	
					if t[ii,jj]==-1:
						pyautogui.moveTo(x+(j+jj+1)*16, y+(i+ii+1)*16, duration=2)
						pyautogui.click(x+(j+jj+1)*16, y+(i+ii+1)*16, clicks=1, interval=0, button='left')


#grafer()
print(tablero)
			
pyautogui.keyDown("alt")  
pyautogui.press("tab")
pyautogui.keyUp("alt")



