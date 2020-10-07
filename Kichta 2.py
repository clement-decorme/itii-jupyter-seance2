class Rectangle :
    def __init__ (self, lon, lar) :
        self.lon = lon
        self.lar = lar
        
    def getLongueur (self) : return self.lon
    def getLargeur (self) : return self.lar
    def setLongueur (self, l) : self.lon = l
    def setLargeur (self, L) : self.lar = L
        
    def Perimetre (self) :
        return self.lon * 2 + self.lar * 2
        
    def Surface (self) :
        return self.lon * self.lar
    
class Parallelepipede (Rectangle) :
    def __init__ (self, lon, lar, hau) :
        self.lon = lon
        self.lar = lar
        self.hau = hau
        
    def Volume (lon, lar, hau) :
        v = self.lon * self.lar * self.hau
        return v

## MonRectangle = Rectangle(5,2)
## print(MonRectangle)
## print(MonRectangle.getLongueur())
