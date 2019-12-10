dic={}
while True:
	n=input("Desea introducir un nuevo contacto")
	if n=="si" or n=="s":
		print("si")
		nombre_prov=input("introduzca el nombre del alumno")
		lista=list(dic.keys())
		pato=True
		for x in range(len(lista)):
			if lista[x]==nombre_prov:
				print("Ese contacto ya ha sido introducido anteriormente, píerdase")
				break
		else:
			nombre=nombre_prov
			numero=input("introduzca el numero del alumno")
			dic[nombre]=numero
	elif n=="no" or n=="n":
		print("Gracias que tenga un buen día")
		print(dic)
		break
	else:
		print("Introduzca si o no")
