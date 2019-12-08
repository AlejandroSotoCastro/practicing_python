
#3. Dado el fichero de texto números.txt realiza un programa en Python
#que recorra el fichero y sume todos los números pares,
#los números están separados por espacios. 

f=open("ejercicio1.txt","r")
r=f.read()
r=r.split()
cont=0
for x in r:
	if int(x)%2==0:
		cont+=int(x)

print(2*cont)

f.close()