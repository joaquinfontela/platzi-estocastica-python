from BorrachoTradicional import BorrachoTradicional
from Campo import Campo
from Coordenada import Coordenada


def caminata(campo, borracho, pasos):
    
    inicio = campo.obtenerCoordenada(borracho)
    
    for _ in range(pasos):
        campo.moverBorracho(borracho)
        
    return inicio.distancia(campo.obtenerCoordenada(borracho))
    # devuelve la distancia desde el inicio (usualmente el 0,0) hasta el lugar donde termino el borracho.


def simularCaminatas(pasos, numeroDeIntentos, tipoDeBorracho):
    
    borracho = tipoDeBorracho(nombre='Joaquin')
    origen = Coordenada( 0, 0 )
    distancias = []
    
    for _ in range(numeroDeIntentos):
        campo = Campo()
        campo.anadirBorracho(borracho, origen)
        simulacionCaminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacionCaminata))
        
    return distancias


def main(distanciasDeCaminata, numeroDeIntentos, tipoDeBorracho):
    
    for pasos in distanciasDeCaminata:
        distancias = simularCaminatas(pasos, numeroDeIntentos, tipoDeBorracho)
        distanciaMedia = round( sum(distancias) / len(distancias), 4 )
        distanciaMaxima = max(distancias)
        distanciaMinima = min(distancias)
        print(f'{tipoDeBorracho.__name__} camino {pasos} pasos, con una distancia media de {distanciaMedia}')
        print(f'La distancia maxima fue de {distanciaMaxima} y la minima de {distanciaMinima}.\n')


if __name__ == "__main__":
    
    distanciasDeCaminata = [ 10, 100, 1000, 10000 ]
    numeroDeIntentos = 100
    
    main(distanciasDeCaminata, numeroDeIntentos, BorrachoTradicional)