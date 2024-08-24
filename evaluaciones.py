from pizza import Pizza
#llama atributos de clase con pizza.atributo
print(f"Precio de la pizza: ${Pizza.precio}")
print(f"Tamaño de la pizza {Pizza.tamaño}")
#valida si la salsa de tomate está dentro de las salsas disponibles, usando el método validar
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa BBQ"]))
#crea una instancia y usa el método realizar_pedido 
p1 = Pizza()
p1.realizar_pedido()
#muestra los ingredientes y si la pizza es válida
print(f"Tipo de masa : {p1.tipo_masa}")
print(f"Ingrediente proteico: {p1.ing_proteico}")
print(f"Ingredientes vegetales: {p1.ing_vegetal1}, {p1.ing_vegetal2}")
if p1.validada == True:
    print("La pizza es válida")
else:
    print("La pizza es inválida")
#genera error al preguntar si la clase Pizza es una clase válida
print({Pizza.validada})
