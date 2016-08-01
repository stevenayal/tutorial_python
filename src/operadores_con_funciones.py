subtotal = 0
porc_descuento = 0
tasa_iva = 0
descuento = 0
subtotal_menos_descuento = 0
importe_iva = 0
total = 0

def solicitar_datos():
    global subtotal
    global porc_descuento
    global tasa_iva
    subtotal = input('Ingrese el subtotal: ')
    porc_descuento = input('Ingrese el descuento: ')
    tasa_iva = input('Ingrese la  tasa de I.V.A: ')	

def calcular_datos():
	global descuento
	global subtotal_menos_descuento
	global importe_iva
	global total
	descuento = subtotal * (porc_descuento / 100.00)
	subtotal_menos_descuento = subtotal - descuento
	importe_iva = subtotal_menos_descuento * (tasa_iva / 100.00)
	total = subtotal_menos_descuento + importe_iva

def imprimir_resultado():
	print "========================="
	print 'Total: ', total
	print 'Descuento: ', descuento
	print 'IVA:', importe_iva

solicitar_datos()
calcular_datos()
imprimir_resultado()
