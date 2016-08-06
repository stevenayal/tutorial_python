# -*- coding: utf-8 -*-#
class Dog():
	name = ''
	def bark(self):
		print "{}, guau... guau... ".format(self.name)
		print


'''---------------------'''
perro1 = Dog()
perro1.name = 'Doqui'

perro2 = Dog()
perro2.name = 'Firulaes'

perro2.bark();
perro1.bark();