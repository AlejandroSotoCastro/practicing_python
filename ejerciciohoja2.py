def func():
	while True:
		a=float(input("introduce numero par y entero"))
		if a%1==0 and a>0:
			break
	num=1
	for x in range(1,int(a)+1):
		num=x*num
		
	return num
print(func())