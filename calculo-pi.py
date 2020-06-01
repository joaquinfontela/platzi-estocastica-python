import random
import math
from introduccion_programacion_estocastica.estadisticas import desviacionEstandar, media

def lanzarAgujas(numeroDeAgujas):
    
    agujasDentroDelCirculo = 0
    
    for _ in range(numeroDeAgujas):
        x = ( random.random() * random.choice([ -1, 1 ]))
        y = ( random.random() * random.choice([ -1, 1 ]))
        distanciaAlCentro = math.sqrt( x ** 2 + y ** 2 )
        
        if distanciaAlCentro <= 1:
            agujasDentroDelCirculo += 1
            
    return ( 4 * ( agujasDentroDelCirculo / numeroDeAgujas ) )


def estimacion(numeroDeAgujas, numeroDeSimulaciones):
    
    estimados = []
    for _ in range(numeroDeSimulaciones):
        estimacionPi = lanzarAgujas(numeroDeAgujas)
        estimados.append(estimacionPi)
        
    mediaEstimados = media(estimados)
    sigma = desviacionEstandar(estimados)
    
    print(f'Estimado de PI = {mediaEstimados}.')
    print(f'Desviacion estandar = {sigma}.')
    print(f'Numero de agujas lanzadas por simulacion = {numeroDeAgujas}.')
    
    return (mediaEstimados, sigma)
    
    
def estimarPi(precision, numeroDeAgujas, numeroDeSimulaciones):
    sigma = precision    
    
    while sigma >= ( precision / 1.96 ):
        # el 1.96 es para tener una confiabilidad del 95%, gracias a la ley de la distribucion normal (campana de gauss)
        #explicacion: https://www.youtube.com/watch?v=2wugQGs1GNY
        media, sigma = estimacion( numeroDeAgujas, numeroDeSimulaciones )
        numeroDeAgujas *= 2
        
    return media


if __name__ == "__main__":
    
    estimarPi(0.01, 1000, 1000)
    #Podemos observar que en cada iteracion la desviacion estandar es mas pequena.