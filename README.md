# Desafío - Métodos y Atributos en Python

Este desafío tiene como objetivo crear un prototipo de aplicación para una cadena de pizzerías que permita a los clientes autogestionar sus pedidos. Utilizando las características de la Programación Orientada a Objetos en Python, se desarrollará un sistema que permita ordenar una pizza con 3 ingredientes y escoger el tipo de masa.

## Requisitos

1. **Clase `Pizza`**  
   Crear una clase `Pizza` que permita crear objetos de tipo Pizza, considerando los atributos de clase adecuados.

   ```python
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
   ```

2. **Método para Validar Ingredientes**  
   Agregar un método estático que permita validar un elemento dentro de una lista de casos posibles. Este método debe recibir dos argumentos: el elemento a validar y los valores posibles.

   ```python
   class Pizza:
       # Código anterior...

       @staticmethod
    def validar(eleccion: str, opciones: list):
        return eleccion in opciones
   ```

3. **Método para Realizar un Pedido**  
   Agregar un método que permita realizar un pedido, solicitando al usuario ingresar el ingrediente proteico, los dos ingredientes vegetales y el tipo de masa.

   ```python
   class Pizza:
       # Código anterior...

       def realizar_pedido(self):
        """Permite realizar un pedido, pide tipo de masa e ingredientes"""
        self.ing_proteico =  input("Ingrese el ingrediente proteico: ").lower()
        self.ing_vegetal1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        self.ing_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa: ").lower()
   ```

4. **Validación del Pedido**  
   Dentro del método `realizar_pedido`, validar los ingredientes y el tipo de masa usando el método del paso 2. Si los valores son válidos, se almacenará un atributo que indique si la pizza es válida.

   ```python
   class Pizza:
       # Código anterior...

       def realizar_pedido(self):
           # Código anterior...

                   self.validada = (self.ing_proteico, i.tipos_proteina) and self.validar(self.ing_vegetal1, i.tipos_vegetal) and self.validar(self.ing_vegetal2, i.tipos_vegetal) and self.validar(self.tipo_masa, i.tipos_masa)
   ```

5. **Archivo `evaluaciones.py`**  
   Crear un archivo que importe la clase `Pizza` y realice las siguientes acciones:

   ```python
    from pizza import Pizza
    from ingredientes import tipos_masa, tipos_proteina, tipos_vegetal

   # a. Mostrar los atributos de clase
    print(f"Precio de la pizza: ${Pizza.precio}")
    print(f"Tamaño de la pizza {Pizza.tamaño}")

   # b. Validar si 'salsa de tomate' está en la lista de salsas
    print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa BBQ"]))

   # c. Crear una instancia de Pizza y solicitar ingredientes
    p1 = Pizza()
    p1.realizar_pedido()

   # d. Mostrar los ingredientes y si es una pizza válida
    print(f"Tipo de masa : {p1.tipo_masa}")
    print(f"Ingrediente proteico: {p1.ing_proteico}")
    print(f"Ingredientes vegetales: {p1.ing_vegetal1}, {p1.ing_vegetal2}")
    if p1.validada == True:
        print("La pizza es válida")
    else:
        print("La pizza es inválida")
   # e. Intentar mostrar si la clase Pizza es una pizza válida

    print({Pizza.validada})  

## Tip

Puedes crear un archivo `ingredientes.py` con listas que contengan los valores de ingredientes proteicos, vegetales, y tipos de masa.

```python
# ingredientes.py

tipos_masa = ["tradicional", "delgada"]
tipos_vegetal = ["tomates", "aceitunas", "champiñones"]
tipos_proteina = ["pollo", "vacuno", "carne vegetal"]
```