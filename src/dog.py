# -*- coding: utf-8 -*-
edad = input('Ingrese la edad del perro: ')
print
if edad < 0:
	print "Edad de perro invalida!!"
elif edad == 1:
	print "Equivalente a 14 años humanos. "
elif edad == 2:
	print "Equivalente a 22 años humanos. "
else:
	edad_humano = 22 + (edad - 2) * 5
	print "Equivalente a %s años humanos" % (edad_humano)
raw_input('Presione cualquier tecla para continuar...')