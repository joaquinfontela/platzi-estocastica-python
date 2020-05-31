from BorrachoTradicional import BorrachoTradicional
from Campo import Campo
from Coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    
    inicio = campo.obtenerCoordenada(borracho)
    #agrego la lista de coordenadas para seguir la posicion del borracho
    coordenadas = []
    
    for _ in range(pasos):
        campo.moverBorracho(borracho)
        coordenadas.append(campo.obtenerCoordenada(borracho))
        
    return inicio.distancia(campo.obtenerCoordenada(borracho)), coordenadas
    # devuelve la distancia desde el inicio (usualmente el 0,0) hasta el lugar donde termino el borracho.


def simularCaminatas(pasos, numeroDeIntentos, tipoDeBorracho):
    
    borracho = tipoDeBorracho(nombre='Joaquin')
    origen = Coordenada( 0, 0 )
    distancias = []
    
    for _ in range(numeroDeIntentos):
        campo = Campo()
        campo.anadirBorracho(borracho, origen)
        simulacionCaminata, coordenadas = caminata(campo, borracho, pasos)
        distancias.append(round(simulacionCaminata))
        
    return distancias, coordenadas
    # devuelve solo la lista de coordenadas del ultimo intento.
    

def generarListaDePosicionesXeY(coordenadas):
    
    coordenadasX = []
    coordenadasY = []
    
    for coordenada in coordenadas:
        coordenadasX.append(coordenada.x)
        coordenadasY.append(coordenada.y)
        
    return coordenadasX, coordenadasY
        


def graficar(x, y):
    grafica = figure(title = 'Camino de Borrachos', x_axis_label='pasos', y_axis_label='distancia recorrida')
    #Creamos una grafica a la cual le damos un titulo, y un nombre a las x e y.
    grafica.line(x, y, legend='distancia media')
    
    show(grafica)
    
    
def graficarPosiciones(x, y):
    
    grafica = figure(title = 'Coordenadas del borracho', x_axis_label='posicion_x', y_axis_label='posicion_y')
    grafica.line(x, y, legend='coordenadas del borracho')
    
    show(grafica)

def main(distanciasDeCaminata, numeroDeIntentos, tipoDeBorracho):
    
    distanciaMediaPorCaminata = []
    # Un array con la distancia media al origen por cada caminata.
    for pasos in distanciasDeCaminata:
        distancias, coordenadas = simularCaminatas(pasos, numeroDeIntentos, tipoDeBorracho)
        distanciaMedia = round( sum(distancias) / len(distancias), 4 )
        #distanciaMediaPorCaminata.append(distanciaMedia)
        distanciaMaxima = max(distancias)
        distanciaMinima = min(distancias)
        print(f'{tipoDeBorracho.__name__} camino {pasos} pasos, con una distancia media de {distanciaMedia}')
        print(f'La distancia maxima fue de {distanciaMaxima} y la minima de {distanciaMinima}.\n')
        
    coordenadasX, coordenadasY = generarListaDePosicionesXeY(coordenadas)
    #genera el grafico de coordenadas solo para el ultimo ejemplo.
    graficarPosiciones(coordenadasX, coordenadasY)


if __name__ == "__main__":
    
    distanciasDeCaminata = [10,100,1000,10000]
    numeroDeIntentos = 1
    
    main(distanciasDeCaminata, numeroDeIntentos, BorrachoTradicional)