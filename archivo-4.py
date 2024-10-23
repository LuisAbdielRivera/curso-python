class Animal:
    def __init__(self, peso, tamanio):
        print(f"Creando animal {peso}, {tamanio}")
    def comer(self):
        print("El animalito come")
    def dormir(self):
        print("El animalito duerme")
    def duerme(self):
        print("El animalito se mueve")

animal = Animal(14, 64)
print(type(animal))

class Perro(Animal):
    def __init__(self, nombre, raza):
        print(f"El perro es: {nombre}, {raza}")

print(Perro.__base__)
mi_perro = Perro(12, 33)
print(mi_perro.comer())

su_perro = Perro ("Boby", "Doverman")