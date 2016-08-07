# -*- coding: utf-8 -*-#
class Dog():  # Definición de clase
	kind = 'PUG'
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
print perro2.kind
perro1.kind = 'Doberman'
perro1.bark();
print 'Raza instancia {}, Raza Clase {}'.format(perro1.kind, Dog.kind)
