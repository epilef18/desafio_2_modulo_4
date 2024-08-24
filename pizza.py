import ingredientes as i
#clase que permite crear objetos tipo pizza
class Pizza():
    #atributos de clase
    precio = 10000
    tamaño = "familiar"

    #almacena atributos de método
    def __init__(self):
        self.ing_proteico = None
        self.ing_vegetal1 = None
        self.ing_vegetal2 = None
        self.tipo_masa = None
        self.validada = False

    #metodo estático, trae la etiqueta de decoracion
    @staticmethod
    def validar(eleccion: str, opciones: list):
        """Permite validar si un texto esta dentro de una lista de textos, retorna un booleano"""
        return eleccion in opciones
    #metodo no estático, trae la etiqueta self en sus variables
    def realizar_pedido(self):
        """Permite realizar un pedido, pide tipo de masa e ingredientes"""
        self.ing_proteico =  input("Ingrese el ingrediente proteico: ")
        self.ing_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ing_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa: ")
        #valida los ingredientes proporcionados por el usuario
        if self.validar(self.ing_proteico, i.tipos_vegetal) and self.validar(self.ing_vegetal1, i.tipos_vegetal) and self.validar(self.ing_vegetal2, i.tipos_vegetal) and self.validar(self.tipo_masa, i.tipos_masa):
            self.validada = True
        else:
            self.validada = False

