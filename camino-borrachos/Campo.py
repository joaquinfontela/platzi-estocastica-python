class Campo:
    
    def __init__(self):
        
        self.coordenadasDeBorrachos = {}
        
        
    def anadirBorracho(self, borracho, coordenada):
        
        self.coordenadasDeBorrachos [borracho] = coordenada
        
        
    def moverBorracho(self, borracho):
        
        deltaX, deltaY = borracho.camina()
        coordenadaActual = self.coordenadasDeBorrachos [borracho]
        nuevaCoordenada = coordenadaActual.mover(deltaX, deltaY)
        
        self.coordenadasDeBorrachos [borracho] = nuevaCoordenada
        
    
    def obtenerCoordenada(self, borracho):
        
        return self.coordenadasDeBorrachos [borracho]