lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[1,2,3,1,1,1,4,1,1,1,1,1,4,4]
lista3=[]
for x in range(len(lista1)):
	for y in range(len(lista2)):
		if lista1[x]==lista2[y]:
			for z in range(len(lista3)):
				if lista1[x]==lista3[z]:
					break
			else:
				lista3.append(lista1[x])

print(lista3)