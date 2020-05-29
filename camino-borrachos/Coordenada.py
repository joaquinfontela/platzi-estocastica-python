class Coordenada:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
        
    def mover(self, deltaX, deltaY):
        
        return Coordenada(self.x + deltaX, self.y + deltaY)
    
    
    def distancia(self, otraCoordenada):
        
        deltaX = self.x - otraCoordenada.x
        deltaY = self.y - otraCoordenada.y
        return (( deltaX ** 2 + deltaY ** 2 ) ** 0.5 )