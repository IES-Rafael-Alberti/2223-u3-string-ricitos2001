'''Ejercicio 3.0.4: Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano'''
#funcion de la definicion
def crear_cuenta(palabra,caracter):
    for letra in palabra:
        if letra == caracter:
            contador=palabra.count(letra)
    return contador

if __name__=="__main__":
    # entrada
    palabra=input("introduce una palabra: ")
    caracter=input("introduce una letra: ")
    # procesamiento
    cuenta=crear_cuenta(palabra,caracter)
    # salida
    print(cuenta)