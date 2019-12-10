import math

a=int(input("introduce el primer coeficiente"))
b=int(input("introduce el segundo coeficiente"))
c=int(input("introduce el tercer coeficiente"))
try:
	x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
	
	print(x)
except:
	print("solucion no real")

try:
	y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
	print(y)
except:
	print("solucion no real")





	




	
