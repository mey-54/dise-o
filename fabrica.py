#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases que hereden de fabrica.
 # las cuales son Moto y Carro.
 #Crear metodos que muestren la calidad de llantas, color y precio de ambos transportes.
 # Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributros de cada uno.
 
 
 class Fabrica:
        def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        print(f"Cantidad de llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio} pesos")

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.10
            self.precio -= descuento
            print(f"Descuento aplicado. Nuevo precio: {self.precio} pesos")
        else:
            print("No se aplica descuento.")

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)

class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)

# Crear objetos de las clases Moto y Carro
moto = Moto("Rojo", 120000)
carro = Carro("Azul", 95000)

# Mostrar atributos y aplicar descuento
print("Moto:")
moto.mostrar_atributos()
moto.aplicar_descuento()

print("\nCarro:")
carro.mostrar_atributos()
carro.aplicar_descuento()
