'''Ejercicio 3.0.1: Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.'''
#funcion de la definicion
def crear_lista(palabra):
    lista = len(palabra[::])
    letras=[]
    while lista != 0:
        letras.append(palabra[lista-1])
        lista-=1
    return letras

if __name__=="__main__":
    #entrada
    palabra= input("dime una palabra: ")
    #procesamiento
    caracter=crear_lista(palabra)
    #salida
    for letras in caracter:
        print (letras)

