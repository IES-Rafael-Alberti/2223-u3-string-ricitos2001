'''Ejercicio 3.0.2: Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?'''
def crear_fruta(listafruta):
    fruta=listafruta[:]
    return fruta
if __name__=="__main__":
    listafruta="fruta"
    fruta=crear_fruta(listafruta)
    print(fruta)
    #fruta[:] es: fruta