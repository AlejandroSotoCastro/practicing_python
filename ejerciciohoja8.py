

def fun(a,b):
	cont=0
	lista2=[]
	for x in a:
		cosa=x
		if cosa.find(b)==0:
			cont+=1
			lista2.append(x)
	
	return lista2


lista=["hola","adios","avion"]
letra="a"
print(fun(lista,letra))
	


	




	
