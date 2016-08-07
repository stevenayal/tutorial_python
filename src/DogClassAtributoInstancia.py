# -*- coding: utf-8 -*-#
class Dog():  # Definición de clase
	color = 'Gris'
	def __init__(self, name):
		self.name = name

	def bark(self):  # <-- metodo para ladrar.
		print "{}, guau... guau... ".format(self.name)

	@property	
	def name(self):
		return self.name

	@name.setter
	def name(self, name):
		self.name = name
	
perro1 = Dog('Doqui')
perro2 = Dog('Firulaes')
perro2.bark();
print perro2.color
perro1.color = 'Negro'
perro1.bark();
print 'Color instancia {}, Color Clase {}'.format(perro1.color, Dog.color)
