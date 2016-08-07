class StringBusquedas:
    def countMethod(self):
        string = "Regresa un entero contando la cantidad de veces que aparece una subcadena. Buscaremos la palabra Regresa:" 
        print string
        print string.count("Regresa")

    def findMethod(self, word):
        string = "Regresa un entero representando la posicion donde inicia la subcadena. Si no la encuentra, retorna -1"
        print string
        string.find(word)

busquedas = StringBusquedas()


busquedas.countMethod()
busquedas.findMethod("entero")
busquedas.findMethod("parangaricutirimicuaro")

