
#1. Crea un fichero llamado ejercicio1.txt 
#donde escribas todos los enteros entre 1 y 1000 separados por espacio. 

f=open("ejercicio1.txt","w")
for n in range(1,1001,1):
	b=str(n)+" "
	f.write(b)
f.close()
f=open("ejercicio1.txt","a")
for n in range(1001,1251):
	b=str(n)+" "
	f.write(b)

f.close()
	