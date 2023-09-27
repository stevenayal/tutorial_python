subtotal = float(input("Ingrese el subtotal: "))
porc_descuento = float(input("Ingrese el descuento: "))
tasa_iva = float(input("Ingrese la  tasa de I.V.A: "))

descuento = subtotal * (porc_descuento / 100.00)
subtotal_menos_descuento = subtotal - descuento
importe_iva = subtotal_menos_descuento * (tasa_iva / 100.00)
total = subtotal_menos_descuento + importe_iva

print ("=========================")
print ("Total: ", total)
print ("Descuento: ", descuento)
print ("IVA:", importe_iva)
