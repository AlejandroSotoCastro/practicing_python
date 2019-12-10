import random
lista=["blanco","rojo","azul","amarillo","rosa","verde"]
cantidad_compras=int(input("Cual es su cantidad de compra en leuros"))
if cantidad_compras < 100:
	print("es usted pobre, larguese")
else:
	descuento=random.choice(lista)

def descuentos(descuento):
	if descuento == "blanco":
		print(cantidad_compras)
	if descuento =="rojo":
		print(0.9*cantidad_compras)
	if descuento =="azul":
		print(0.85*cantidad_compras)
	if descuento =="amarillo":
		print(0.8*cantidad_compras)
	if descuento =="rosa":
		print(0.75*cantidad_compras)
	if descuento =="verde":
		print(0.7*cantidad_compras)

descuentos(descuento)