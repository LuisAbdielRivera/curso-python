# Auto: Avanzar, Frenar, Apagar, Encender, GirarIzq, GirarDer
def automovil():
    estado = 'apagado'
    def encender():
        nonlocal estado
        if estado == 'apagado':
            print('Encendiendo')
            estado = 'encendido'
        else:
            print('El automóvil está encendido')
    def apagar():
        nonlocal estado
        if estado == 'encendido':
            print('Apagando')
            estado = 'apagado'
        else:
            print('El automóvil ya está apagado')
    def avanzar():
        if estado == 'encendido':
            print('Avanzando')
        else:
            print('El automóvil debe estar encendido para avanzar')
    def frenar():
        if estado == 'encendido':
            print('Frenando')
        else:
            print('El automóvil debe estar encendido para frenar')
    def girar_izquierda():
        if estado == 'encendido':
            print('Girando a la izquierda')
        else:
            print('El automóvil debe estar encendido para frenar')
    def girar_derecha():
        if estado == 'encendido':
            print('Frenando')
        else:
            print('Girando a la derecha')
