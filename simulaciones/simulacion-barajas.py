import random
from collections import Counter

PALOS = [ 'ESPADAS', 'TREBOLES', 'DIAMANTES', 'CORAZONES' ]
VALORES = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]

def crearMazo():
    mazo = []
    for palo in PALOS:
        for valor in VALORES:
            mazo.append(( palo, valor ))
            
    return mazo


def obtenerMano(mazo, cantidadCartas):
    
    return random.sample(mazo, cantidadCartas)
    #sample devuelve 'cantidadCartas' de elementos random de 'mazo', pero sin repetirse entre ellos.
    #si le pedimos mas elementos de los que trae el array, lanza error.
    
    
def hayPar(valoresDeLasCartas):
    #Devuelve True si hay al menos un par en la mano (recibe solo los valores de las cartas).
    contador = dict(Counter(valoresDeLasCartas))
    ''' 
    Counter devuelve un diccionario en el que cada valor en la mano es una clave, y los valores del
    diccionario son la cantidad de apariciones de cada valor de las cartas en dicha mano.
    '''
    return (2 in contador.values())
    
    
    
def obtenerProporcionDePares(manos):
    # Recibe un conjunto de manos y devuelve la proporcion (entre 0 y 1) de esas manos que son pares.
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append( carta[1] )
            # por cada carta en la mano, guardo en el array el valor de esta.
        
        if hayPar( valores ):
            pares += 1
            
    return ( pares / len( manos ))


def hayTrio(valoresDeLasCartas):
    #Devuelve True si hay al menos un trio en la mano (recibe solo los valores de las cartas).
    contador = dict(Counter(valoresDeLasCartas))
    return (3 in contador.values())


def obtenerProporcionDeTrios(manos):
    # Recibe un conjunto de manos y devuelve la proporcion (entre 0 y 1) de esas manos que son trios.
    trios = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append( carta[1] )
            # por cada carta en la mano, guardo en el array el valor de esta.
        
        if hayTrio( valores ):
            trios += 1
            
    return ( trios / len( manos ))


def obtenerEscalerasPosibles():
    # devuelve una lista con todas las escaleras posibles.
    escaleras = []
    for i in range(9):
        escaleras.append(VALORES[i:i+5])
    escaleras.append([ '10', 'J', 'Q', 'K', 'A' ])
    return escaleras


def hayEscalera(valoresDeLasCartas):
    #Devuelve True si hay al menos una escalera en la mano (recibe solo los valores de las cartas).
    escalerasPosibles = obtenerEscalerasPosibles()
    for escalera in escalerasPosibles:
        if set(escalera).issubset(set(valoresDeLasCartas)):
            return True
            ''' 
            Genera un conjunto con los valores de la escalera, y pregunta si es esta es un
            subconjunto de los valores de las cartas recibidos.
            '''
    
    return False


def obtenerProporcionDeEscaleras(manos):
    # Recibe un conjunto de manos y devuelve la proporcion (entre 0 y 1) de esas manos que son escaleras.
    escaleras = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append( carta[1] )
            # por cada carta en la mano, guardo en el array el valor de esta.
        
        if hayEscalera( valores ):
            escaleras += 1
            
    return ( escaleras / len( manos ))
    
    
    
def main(cantidadCartas, numeroDeSimulaciones):
    
    mazo = crearMazo()
    manos = []
    
    for _ in range(numeroDeSimulaciones):
        manos.append(obtenerMano(mazo, cantidadCartas))
        
    proporcionDePares = obtenerProporcionDePares(manos)
    print(f'La probabilidad de obtener un par en {cantidadCartas} cartas es de {proporcionDePares}.')
    
    proporcionDeTrios = obtenerProporcionDeTrios(manos)
    print(f'La probabilidad de obtener un trio en {cantidadCartas} cartas es de {proporcionDeTrios}.')
    
    proporcionDeEscaleras = obtenerProporcionDeEscaleras(manos)
    print(f'La probabilidad de obtener una escalera en {cantidadCartas} cartas es de {proporcionDeEscaleras}.')        
    
        



if __name__ == "__main__":
    
    cantidadCartas = int(input('De cuantas cartas sera la mano? '))
    numeroDeSimulaciones = int(input('Cuantas simulaciones para calcular la probabilidad? '))
    
    main(cantidadCartas, numeroDeSimulaciones)