a=int(input("Cuántos números se van a introducir"))
neg=0
menor=0
mayor=0
x=int(input("Introduce un numero"))
menor=x
mayor=x
num=x

if x<0:
	neg+=1
for n in range(a-1):
	if x<0:
		neg+=1
	x=int(input("Introduce un numero"))
	num+=x
	
	if x>mayor:
		mayor=x
	else:
		if x<menor:
			menor=x
	

print(num/a)
print(mayor)
print(menor)
print(neg)