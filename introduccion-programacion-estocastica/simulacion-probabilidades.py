import random


def tirarDado():
    #Simula un tirada de un dado.
    return random.choice([ 1, 2, 3, 4, 5, 6 ])


def tirarDados(cantidadDeDados):
    #Simula una tirada de una cantidad de dados.
    sumaDados = 0
    for dado in range(cantidadDeDados):
        sumaDados += tirarDado()
        
    return sumaDados
        

def tirarDadosUnaCantidadDeVeces(numeroDeTiros):
    # Simula una cantidad de tiradas de dados y devuelve una lista con los valores de esas tiradas.
    secuenciaDeTiros = []
    
    for tiro in range(numeroDeTiros):
        
        valor = tirarDados(2)
        secuenciaDeTiros.append(valor)
    
    return secuenciaDeTiros


def obtenerSimulacionesEnLasQueSalioElNumero(numero, secuenciasDeTiros):
    '''
    Devuelve la cantidad de secuencias dentro de secuenciasDeTiros en las que el numero obtenido
    en el primer parametro salio.
    '''
    cantidadDeSimulacionesEnLasQueSalioElNumero = 0
    for secuenciaDeTiros in secuenciasDeTiros:
        if numero in secuenciaDeTiros:
            cantidadDeSimulacionesEnLasQueSalioElNumero += 1
            
    return cantidadDeSimulacionesEnLasQueSalioElNumero
            

def main(numeroDeTiros, numeroDeSimulaciones):
    #Realiza una cantidad de simulaciones en las que en cada una se realiza una cantidad de tiros definida en el primer par.
    secuenciasDeTiros = []
    
    for simulacion in range(numeroDeSimulaciones):
        
        secuenciaDeTiros = tirarDadosUnaCantidadDeVeces(numeroDeTiros)
        secuenciasDeTiros.append(secuenciaDeTiros)
        
    numero = 7
    cantidadDeSimulacionesEnLasQueSalioElNumero = obtenerSimulacionesEnLasQueSalioElNumero(numero, secuenciasDeTiros)
    
    probabilidadDeObtenerAlMenosUnaVezElNumero = cantidadDeSimulacionesEnLasQueSalioElNumero / numeroDeSimulaciones
    print(f'La probabilidad de que salga un {numero} en una simulacion con {numeroDeTiros} tiros es: {probabilidadDeObtenerAlMenosUnaVezElNumero}.')
    
    
if __name__ == '__main__':
    
    numeroDeTiros = int(input('Cuantas veces queres tirar el dado? '))
    numeroDeSimulaciones = int(input('Cuantas simulaciones queres hacer? '))
    
    main(numeroDeTiros, numeroDeSimulaciones)
    