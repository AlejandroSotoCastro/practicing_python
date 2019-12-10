


def entero():
	while True:
		a=float(input("Introduce un numero entero"))
		if a%1!=	0:
			print("eso no es entero, mamon")
			continue
		else:
			return int(a)
a=entero()
b=0
while True:
	if b>a:
		break
	else:
		b+=entero()
	




	
