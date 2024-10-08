print('Bienvenido a Python')

a = 2
print(a)

b = 5.4
print(b)

c = 'Clase de seguridad'
print(c)

#Este simbolo representa un comentario

'''
En esta seccion se crea un comentario multilinia
print(c)
'''

#Operadores Aritmeticos
d = a + b
print(d)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Sintaxis de Condicionales
edad = 16
if edad > 18:
    print('Mayor de edad')
else:
    print('Menor de edad')

e, f, g = 3, 8, 9
print((e + f)*g)

imprimir = True

if imprimir:
    print('El valor de la operación es:', (e + f)*g)
else:
    print('No esta permitido imprimir')

h = 1 + 2 + 3 + 4 + 5+\
6 + 7 + 8
print(h)

i = (1 + 2 + 3 + 4 + 5+
6 + 7 + 8)
print(i)

def suma (j, k):
    return (j + k)
print(suma(8,9))