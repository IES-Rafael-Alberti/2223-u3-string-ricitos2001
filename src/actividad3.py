'''Ejercicio 3.0.3: Tienes este código:
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.'''
# funcion de la definicion
def crear_cuenta(palabra,caracter):
    contador=0
    for letra in palabra:
        if letra == caracter:
            contador = contador + 1
    return contador

if __name__=="__main__":
    # entrada
    palabra=input("introduce una palabra: ")
    caracter=input("introduce una letra:")
    # procesamiento
    cuenta=crear_cuenta(palabra,caracter)
    # salida
    print(cuenta)