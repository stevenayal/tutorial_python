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
			resultado += Int(n)
		return resultado

	def promedio(self):
		resultado = 0
		for n in self.numbers:
			resultado += Int(n)
		return resultado

misNumeros = NumberContainers()
misNumeros.agregar(5)
misNumeros.agregar(1)
misNumeros.agregar(50)
misNumeros.agregar(100)
misNumeros.agregar(104)
misNumeros.agregar(20)
print "El mayor es  {}".format(misNumeros.mayor())
		