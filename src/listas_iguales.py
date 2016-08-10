# -*- encoding: utf-8 -*-

def list_equal(l1, l2):
	if len(l1) != len(l2):
		return False
	for i in range(len(l1)-1):
		if l1[i] != l2[i]:
			return False
	return True

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print 'Lista 1', lista1
print 'lista 2', lista2
print list_equal(lista1, lista2)

lista2 = [3, 2, 1]
print list_equal(lista1, lista2)
