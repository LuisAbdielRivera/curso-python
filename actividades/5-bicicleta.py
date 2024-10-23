class Bicicleta:
    def __init__(self, tipo_sillon, num_rin, diam_rueda, tipo_color):
        print(f"Creando la bicicleta {tipo_sillon}, {num_rin}, {diam_rueda}, {tipo_color}")
    def frenar(self):
        print("La bicicleta freno")
    def girar(self):
        print("Girando")
    def pedalear(self):
        print("Pedaleando..")
    def avanzar(self):
        print("La bicicleta esta avanzando")

mi_bicicleta = Bicicleta("Cuero", 33, 26, "Naranja")
print(mi_bicicleta.avanzar())