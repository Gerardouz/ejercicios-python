





class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.hijos = []

class Arboln:
	def __init__(self):
		self.__raiz = None
				
	def __buscar (self, valor, hermanos = None, pos = 0):
		
		if (pos >= len(hermanos)):
			return None
		
		if (hermanos[pos].info == valor):
			return hermanos[pos]
			
		nodo = self.__buscar (valor, hermanos[pos].hijos, 0)
		if (nodo != None):
			return nodo
		
		nodo = self.__buscar (valor, hermanos, pos + 1)
		if (nodo != None):
			return nodo
		
		return None
		
	def buscar (self, valor):
		
		if (self.__raiz== valor):
			return True
		
		if (self.__buscar(valor, self.__raiz.hijos, 0) != None):
			return True
		return False
		
	def insertar(self, valor, val_padre = None, pos_hijo = 0):
		
		if (self.__raiz == None):
			self.__raiz = Nodo(valor)
			return True
				
		if (val_padre == self.__raiz.info):
			padre = self.__raiz
		else:
			padre = self.__buscar (val_padre, self.__raiz.hijos, 0)
		
		if (padre != None):
			padre.hijos.insert (pos_hijo,Nodo(valor))
			return True
		
		return False
			
	
	def preorden(self, nodos = None, pos = 0):
		
		if (nodos == None):
			if (self.__raiz == None):
				return
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 
		
		print nodos[pos].info, 
		self.preorden(nodos[pos].hijos, 0)
		self.preorden(nodos, pos + 1)
		

	"""
	Equipo 3:
	Gerardo Uzcategui
	Maria Colmenares
	Marbelis Zambrano
	Emmanuel Pineda 


	"""




	#Retorna True o False dependiendo si dos valores pasados por parametro son hermanos

	def hermanos(self,n1,n2,nodos = None,pos = 0):

		if (nodos == None):
			if (self.__raiz == None):
				return False
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 
		g,h = False,False
		for i in nodos:

			if (i.info == n1):

				g = True

			if (i.info == n2):
				h = True
		if (g and h ):
			return True
		

		g =  self.hermanos(n1,n2,nodos[pos].hijos,0)
		
		h =  self.hermanos(n1,n2,nodos, pos + 1)

		if (g or h ):

			return True
		

		return False
		
		

		







# PRINCIPAL

a = Arboln()

#si el arbol esta vacio retorna False

print "arbol vacio \n"
print a.hermanos(7,5), "\n"


b = Arboln()
b.insertar(5)
# si el arbol tiene un solo elemento (la raiz) tambien retorna False
print "un solo elemento \n"
print b.hermanos(5,6), "\n"



c = Arboln()

c.insertar(2)
c.insertar(4,2)
c.insertar(5,2)
# si los valores dados por parametro no existen retorna False
print "los valores no estan en el arbol \n"
print c.hermanos(7,8), "\n"


d = Arboln()

d.insertar(7)
d.insertar(2,7)
d.insertar(5,7)

# si los valores dados por parametro son los hijos de la raiz retorna True

print "hijos de la raiz \n"
print d.hermanos(2,5), "\n"


e = Arboln()

e.insertar(8)
e.insertar(5,8)
e.insertar(4,8)
e.insertar(2,8)
e.insertar(6,5)
e.insertar(0,5)
e.insertar(10,4)
e.insertar(11,4)
e.insertar(3,2)
e.insertar(20,2)

#si los valores dados por parametro son hermanos en cualquier parte del arbol retorna True
print "si son hermanos en un arbol mas grande"

print e.hermanos(3,20), "\n"

f = Arboln()

f.insertar(8)
f.insertar(4,8)
f.insertar(2,8)
f.insertar(0,8)
f.insertar(1,8)
f.insertar(9,4)

#si los valores existen pero no son hermanos retorna False

print "si no son hermanos \n"

print f.hermanos(0,9), "\n"