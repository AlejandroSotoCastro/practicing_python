import random



def crearvector(n):
	vector=[]
	for a in range(n):
		vector.append(random.randint(0,10))
	return vector
	

def ordenarvector(n):
	vector=crearvector(n)
	print(vector)
	x=0
	for z in range(n):
		for m in range(z,n):
			if vector[m]>vector[z]:
				x=vector[z]
				vector[z]=vector[m]
				vector[m]=x	
	return vector

print(ordenarvector(15))




	
