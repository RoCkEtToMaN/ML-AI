class Triangle:
    
    """Classe per calcolare le misure del Triangolo"""
    def __init__(self, a, b, c, h):
        self.a=a
        self.b=b
        self.c=c
        self.h=h
        #self.a,self.b,self.c,self.h = a,b,c,h
        
  
  
    def area(self):        
        """ Calcolo area """  
        return (self.b*self.h)/2

    
    def perimetro(self):        
        """ Calcolo perimetro """   
        return self.a+self.b+self.c
    
    
    
class Square:
    
    """Classe per calcolare le misure del Quadrato"""
    
    def __init__ (self,l):
        self.l = l
        
    
    
    def area(self):
        """ Calcolo area """
        return (self.l)**2
    
    
   
    def perimetro(self):
        """ Calcolo perimetro """ 
        return self.l*4
    
class Rectangle:
    
    """ Classe per calcolare le misure del Rettangolo"""
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def area(self):
        """Calcolo area"""
        return self.a*self.b
    
    def perimetro(self):
        """Calcolo perimetro"""
        return (self.a+self.b)*2
    
 
    
    
 

 