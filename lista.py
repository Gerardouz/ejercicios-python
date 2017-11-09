class Nodo:
  def __init__(self,v):
    self.valor = v
    self.sig = None
class lista:
  


  def __init__(self):
    
    self.__primero = None
    self.__ultimo = None
  def vacio(self):
    if(self.__primero == None):
      return True
    
    
  def insertar(self,v):
    
    
      nodo = Nodo(v)
      
      if (self.vacio() == True):
        self.__primero = nodo 
        self.__ultimo = nodo
        
      else:
        nodo.sig = self.__primero
        self.__primero = nodo
        
      
  def mostrar(self):
    if self.vacio() == True:
      print "la lista esta vacia"
      return
    nodo = self.__primero
    while nodo != None:
      print nodo.valor
      nodo = nodo.sig
  def elimprimer(self):
    if (self.vacio() == True):
      print "lista vacia, imposible eliminar"
      return
      
    if (self.__primero == self.__ultimo):
      self.__primero = None
      self.__ultimo = None
      print "elemento eliminado"
      return
    aux = self.__primero
    self.__primero = self.__primero.sig
    aux = None
    print "elemento eliminado"
  
    
    
    
    
    
        
    
    
      
  
      
 
      



#principal

l = lista()
l.insertar(4)
l.insertar(7)
l.insertar(9)
l.insertar(10)
l.elimprimer()

l.mostrar()