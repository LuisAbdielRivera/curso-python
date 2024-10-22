# Auto: Avanzar, Frenar, Apagar, Encender, GirarIzq, GirarDer
def Avanzar():
    if llave:
        print("Avanzando")
    else:
        print("Inserta la llave")

def Encender():
        global llave
        llave = True

def Apagar():
        global llave
        llave = False
        print("Auto apagado")

def GirarDer():
        print("Girando a la Derecha")
        global gDerecha
        global gIzquierda
        gDerecha = True
        if gDerecha:
                print("Ëstas girando a la derecha, no puedes girar a la Izquierda")
                gIzquierda = False

def GirarIzq():
        print("Girando a la Izquierda")
        global gDerecha
        global gIzquierda
        gIzquierda = True
        if gIzquierda:
                print("Ëstas girando a la izquierda, no puedes girar a la Derecha")
                gDerecha = False

def Frenar():
        print("Parar Auto")

Encender()
Avanzar()
GirarDer()
GirarIzq()
Frenar()
Apagar()