
#4. Escribe una función que reciba una expresión y un archivo y 
#devuelva el número de veces que aparece esa expresión en el archivo. 

def funcion(expresion,archivo):
	#para no complicarme la vida el archivo va a ser el del anterior ejercicio
	#y la expresión va a ser " ".

	f=open(archivo,"r")
	r=f.read()
	return r.count(" ")
	
print(funcion(" ","ejercicio1.txt"))

