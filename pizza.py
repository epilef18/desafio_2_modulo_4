import ingredientes as i
#clase que permite crear objetos tipo pizza
class Pizza():
    #atributos de clase
    precio = 10000
    tamaño = "familiar"

    #almacena atributos de método
    def __init__(self):
        """
        Inicializa una nueva instancia de Pizza.
        Los atributos de instancia se establecen en None por defecto.
        """
        self.ing_proteico = None
        self.ing_vegetal1 = None
        self.ing_vegetal2 = None
        self.tipo_masa = None
        self.validada = False

    #metodo estático, trae la etiqueta de decoracion
    @staticmethod
    def validar(eleccion: str, opciones: list):
        """
        Método estático que valida si una opción está dentro de una lista de opciones.
        
        :param eleccion: Texto a validar.
        :param opciones: Lista de opciones válidas.
        :return: True si eleccion está en opciones, False en caso contrario.
        """ 
        return eleccion in opciones
    #metodo no estático, trae la etiqueta self en sus variables
    def realizar_pedido(self):
        """
        Permite al usuario realizar un pedido de pizza.
        Pide al usuario que ingrese los ingredientes y tipo de masa.
        Valida los ingredientes proporcionados por el usuario utilizando las listas de opciones de 'ingredientes'.
        """
        self.ing_proteico =  input("Ingrese el ingrediente proteico: ").lower()
        self.ing_vegetal1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        self.ing_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa: ").lower()
        #valida los ingredientes proporcionados por el usuario
        self.validada = (self.ing_proteico, i.tipos_proteina) and self.validar(self.ing_vegetal1, i.tipos_vegetal) and self.validar(self.ing_vegetal2, i.tipos_vegetal) and self.validar(self.tipo_masa, i.tipos_masa)
            

