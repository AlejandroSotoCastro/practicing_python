
#2. Modifica el fichero anterior y añádele 250 números más (entre 1001 y 1250

f=open("ejercicio1.txt","a")
for n in range(1001,1251):
	b=str(n)+" "
	f.write(b)

f.close()