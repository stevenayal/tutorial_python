# -*- coding: utf-8 -*-#
class Dog():  # Definición de clase
	__name = ''  # <--- propiedad nombre
	
	def bark(self):  # <-- metodo para ladrar.
		print "{}, guau... guau... ".format(self.getName())
		print

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

''' Instancia de clase perro Doqui '''
perro1 = Dog()
perro1.setName('Doqui')

''' Instancia de clase perro Firulaes '''
perro2 = Dog()
perro2.setName('Firulaes')

''' Perros ladran '''
perro2.bark();
perro1.bark();