class StringsFormat:
    def capitalizeMethod(self):
        string = "bienvenido a la seccion de manejo de strings"
        print "El metodo capitalize convierte a mayusculas el primer caracter de un string" 
        print string.capitalize()

    def lowerMethod(self):
        string = "El METODO lower CONVIERTE a Minusculas LOS CARACTERES DE UN STRING"
        print string.lower()

    def upperMethod(self):
        string = "el metodo upper convierte el string  mayusculas"
        print string.upper()

    def swapcaseMethod(self):
        string = "el metodo SWAPCASE convierte las letras mayusculas a minusculas y viceversa"
        print string.swapcase()

    def titleMethod(self):
        string = "convierte un string en formato de titulo"
        print string.title()

    def centerMethod(self, longitud, caracterRelleno):
        string =  "Regresa una copia de la cadena centrada"
        print string.center(longitud, caracterRelleno)
        print string.center(longitud, " ")

    def ljustMethod(self, longitud, caracterRelleno):
        string =  "Regresa una copia de la cadena alineada a la izquierda"
        print string.ljust(longitud, caracterRelleno)
        print string.ljust(longitud, " ")

    def rjustMethod(self, longitud, caracterRelleno):
        string =  "Regresa una copia de la cadena alineada a la derecha"
        print string.rjust(longitud, " ")

    def zfillMethod(self, longitud):
        folio = 2157
        print "Rellena la cadena con ceros hasta alcanzar la longitud indicada"
        print str(folio).zfill(longitud)

formats = StringsFormat()

formats.capitalizeMethod()
formats.lowerMethod()
formats.upperMethod()
formats.swapcaseMethod()
formats.titleMethod()
formats.centerMethod(50, "=")
formats.ljustMethod(50, "=")
formats.rjustMethod(50, "=")
formats.zfillMethod(50)

