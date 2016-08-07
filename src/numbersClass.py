# -*- coding: utf-8 -*-#
class NumberContainers(object):
	numbers = []

	def __init__(self):
		self.numbers = []
	
	def agregar(self, n):
		self.numbers.append(n);

	def mayor(self):
		mayor = None
		for n in self.numbers:
			if n > mayor:
				mayor = n
		return mayor

	def sumatoria(self):
		resultado = 0
		for n in self.numbers:
			resultado += n
		return resultado

	def promedio(self):
		resultado = 0
		if len(self.numbers):
			resultado = float(self.sumatoria()) / len(self.numbers)
		return resultado

misNumeros = NumberContainers()
while True:
	n = input('Ingrese el número (-1 salir): ')
	if(n == -1):
		break;
	misNumeros.agregar(n)

print "El mayor es  {}".format(misNumeros.mayor())
print "La sumatoria es  {}".format(misNumeros.sumatoria())
print "El promedio es {:5.2f}".format(misNumeros.promedio())
		