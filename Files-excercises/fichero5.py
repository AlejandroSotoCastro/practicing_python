
#5. Escribe una función que devuelva el número de letras en mayúscula
# que hay en un fichero. 
archivo="archivo-txt"
f=open(archivo,"w")
f.write("hoLA")
f.close()


def funcion(archivo):
	f=open(archivo,"r")
	cont=0
	l=f.read()
	for x in l:	
		if x.isupper():
			cont+=1
	return cont
	
print(funcion(archivo))

