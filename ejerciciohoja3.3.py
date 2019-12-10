
def func():

	a=int((input("introduce enumero entre 0 y 9999")))
	b=str(a)
	
	#No me apetece nada optimizar esto asi que lo voy a hacer a lo cutre
	if a>9 and b[0]==b[1]:
		print("es capicua")
		
	if a>99 and b[0]==b[2]:
		print("es capicua")
	if a>999 and b[0]==b[3] and b[1]==b[2]:
		print("es capicua")
func()
	





	




	
