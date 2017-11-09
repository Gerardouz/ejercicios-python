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
			
		nodo = self.__buscar (valor, hermanos[pos].hijos)
		if (nodo != None):
			return nodo
		
		nodo = self.__buscar (valor, hermanos, pos + 1)
		if (nodo != None):
			return nodo
		
		return None
		
	def buscar (self, valor):
		
		if (self.__raiz == valor):
			return True
		
		if (self.__buscar(valor, self.__raiz.hijos) != None):
			return True
		return False
		
	def insertar (self, valor, val_padre = None, pos_hijo = 0):
		
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
	
	# Retorna la informacion del padre con mas hijos 
	def padre_mas_hijos (self, nodos = None, pos = 0):
		
		if (nodos == None):
			if (self.__raiz == None):
				return None
			nodos = [self.__raiz]
			self.__mayorpadre = self.__raiz
		
		if (pos >= len(nodos)):
			return 0
			
		if (len(nodos[pos].hijos) > len(self.__mayorpadre.hijos)):
			self.__mayorpadre = nodos[pos] 
		
		self.padre_mas_hijos(nodos[pos].hijos)
		self.padre_mas_hijos(nodos, pos + 1)
		
		return self.__mayorpadre.info
	
	# Retorna el nro de hijos unicos (sin hermanos) en el arbol 
	# La raiz siempre es hijo unico
	def hijos_unicos (self, nodos = None, pos = 0):
		if (nodos == None):
			if (self.__raiz == None):
				return 0
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 0
		
		h_unico = 0
		if (len(nodos) == 1):
			h_unico = 1
			
		h_unicos_hijos = self.hijos_unicos (nodos[pos].hijos)
		h_unicos_Hermanos = self.hijos_unicos (nodos, pos + 1)
	
		return h_unico + h_unicos_hijos + h_unicos_Hermanos
	
	# Retorna True si dos valores indicados son nodos hermanos en el arbol n-ario
	def son_hermanos (self, fulano, sutano, nodos = None, pos = 0):
		if (nodos == None):
			if (self.__raiz == None):
				return False
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return False
		
		hermano = None
		if (fulano == nodos[pos].info): # Existe Fulano
			hermano = sutano
		elif (sutano == nodos[pos].info): # Existe Mengano
			hermano = fulano
			
		if (hermano != None): # Buscar el hermano si exite fulano o sutano
			for nodo in nodos:
				if (hermano == nodo.info): # Encuentra al hermano
					return True
			
		encontro = self.son_hermanos(fulano,sutano,nodos[pos].hijos)			
		if (encontro):
			return True
		
		return self.son_hermanos(fulano,sutano,nodos, pos + 1)		
	
	# Recorrido en Preorden 
	def preorden (self, nodos = None, pos = 0):
		
		if (nodos == None):
			if (self.__raiz == None):
				return
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 
		
		print nodos[pos].info, 
		self.preorden (nodos[pos].hijos)
		self.preorden (nodos, pos + 1)
		



	def hermanos(self,n1,n2,nodos = None,pos = 0):

		if (nodos == None):
			if (self.__raiz == None):
				return False
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return False
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

		if g == True or h == True:

			return True
		

		return False

		
	#nodos sin hijos 
	def nodos_sin_hijos(self,nodos = None,pos = 0):

		if (nodos == None):
			self.__cont = 0
			if (self.__raiz == None):
				return 0
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 0

		if (nodos[pos].hijos != None and len(nodos[pos].hijos) == 0):
			self.__cont = self.__cont + 1

		self.nodos_sin_hijos(nodos[pos].hijos,0)

		self.nodos_sin_hijos(nodos,pos + 1)

		return self.__cont

	def nivel(self,valor, nodos = None, pos = 0,Nivel = 0):


		if (nodos == None):
			
			if (self.__raiz == None):
				return False
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return False

		if (valor == nodos[pos].info):
			return Nivel

		
		h = self.nivel(valor,nodos[pos].hijos,0,Nivel + 1)
		if (h != None):
			return h
		return self.nivel(valor,nodos,pos + 1,Nivel)






	def nivel_mas_nodos(self, nodos = None, pos = 0, Nivel = 0):

		if (nodos == None):
			self.__nodos = 0
			self.__nivel = 0
			if (self.__raiz == None):
				return 
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return

		if (len(nodos) > self.__nodos):

			self.__nodos = len(nodos)
			self.__nivel = Nivel

		self.nivel_mas_nodos(nodos[pos].hijos,Nivel + 1)
		self.nivel_mas_nodos(nodos, pos + 1,Nivel)

		return self.__nivel

		 

		


		







# PRINCIPAL

a = Arboln()
a.insertar(5)
a.insertar(7,5)
"""a.insertar(0,5)
a.insertar(6,5)
a.insertar(4,7)
a.insertar(2,7)
a.insertar(1,0)
a.insertar(3,0)"""


print a.nodos_sin_hijos()



