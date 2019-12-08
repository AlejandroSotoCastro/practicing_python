
#7. Haz que se muestre por pantalla el fichero creado en el apartado anterior 
archivo="archivo-txt"
f=open(archivo,"r+")


a=0
while True:
	a=input()
	if a=="fin":
		break
	f.write(a)

f.close()

f=open(archivo,"r")
print(f.read())
