#Bucles: While, For, Breack, Comtinue

#Ciclo while
x = 0
while x < 3:
    print(x)
    x+=1

#Ciclo for
print ("Ciclo for")
for i in range(5):
    print(i)

#Ciclo for implementando salto
print ("Ciclo for utilizando continue")
for i in range(6):
    if i == 4:
        continue
    print(i)

#Ciclo while instruccion para finalizar una ejecución
x = 0
while True:
    print(x)
    if x == 50:
        break
    x+=1

#Manejo de excepciones assert, try, except, finally, raise
print("Manejo de excepciones")
x = "10"
valor = None
try: 
    valor = int(x)
    b = 3
    res = valor + b
except Exception as e:
    print("Existe un error:", e)
finally:
    print("El resultado es:", res)

#Variables locales, variables globales y nonlocal en Python
a = 0
def suma_uno():
    global a
    for i in range(6):
        a = a + 1
    print(a)

suma_uno()
print(a)
