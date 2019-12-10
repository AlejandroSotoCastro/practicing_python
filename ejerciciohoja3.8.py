def bin(n):
	resultado=[]
	for x in range(7,-1,-1):
		print(x)
		if n>=2**x:
			resultado.append(1)
			n-=2**x
		else:
			resultado.append(0)
		
	return resultado
print(bin(144))


	




	
