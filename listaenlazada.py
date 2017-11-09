class Nodo:
  def __init__(self,v):
    self.valor = v
    self.sig = None
class lista:
  


  def __init__(self,*v):
    
    self.primero = None
    self.insertar(*v)
    
  def insertar(self,*v):
    
    for j in v:
      nodo = Nodo(v)
      
      if (self.primero != None):
        nodo.sig = self.primero
        
      self.primero = nodo
      return
  def mostrar(self,pos = None):
    nodo = self.primero
    cont = 0
    while (nodo != None):
      if (pos == None):
        print nodo.valor
        
      elif (pos == cont):
        print nodo.valor
        return
      nodo = nodo.sig
      cont = cont + 1
      
  def eliminar(self):
    if (self.primero != None):
      self.primero = self.primero.sig
    else:
      print "lista vacia"
  def sumar(self,lista):
    
    
    
    
    
    
    
    
    return self
    
    
    
    
      
# principal
l1 = lista(1,2,3)
l2 = lista(4,5,6)

l3 = l1.sumar(l2)

l3.mostrar()
