
cantidad_dinero=resto=10.86*100
a=0
monedas=[100,50,20,10,5,1]
cantmoneda=[0,0,0,0,0,0]

for x in monedas:
	cantmoneda[a]=resto//x
	resto=resto-cantmoneda[a]*x
	a+=1
print(cantmoneda)

	




	
