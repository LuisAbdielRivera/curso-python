'''Realizar un programa que permita agregar la edad 
y te indique si la persona es menor de 12 es niño, 
si la persona es mayor a 12 y menor a 17 es adolecente,
si la persona es mayor a 17 y menor a 29 es joven,
si la persona es mayor a 29 y menor a 55 es adulto y
si la persona es mayor a 55 es de la tercera edad'''

edad = 30
if edad < 11:
    print('Eres un niño')
elif edad > 12 and edad < 17:
    print('Eres un adolecente')
elif edad > 17 and edad < 29:
    print('Eres un joven')
elif edad > 29 and edad < 55:
    print('Eres un adulto')
else:
    print('Eres de la tercera edad')