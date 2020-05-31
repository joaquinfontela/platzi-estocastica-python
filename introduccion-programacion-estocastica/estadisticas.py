import math
import random
from media import media

def varianza(X):
    #Devuelve la varianza del conjunto de valores X.
    mu = media(X)
    acumulador = 0
    
    for x in X:
        acumulador += (( x - mu ) ** 2 )
        
    return ( acumulador / len(X) )


def desviacionEstandar(X):
    #Devuelve la desviacion estandar del conjunto de valores X.
    return ( math.sqrt( varianza(X) ))
    
    
if __name__ == "__main__":
    
    X = [ random.randint( 1, 20+1 ) for i in range(20) ]
    #genera un array con 20 valores entre el 1 y el 20
    mu = media(X)
    Var = varianza(X)
    sigma = desviacionEstandar(X)
    
    print(f'Arreglo = {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {sigma}')
    
    
