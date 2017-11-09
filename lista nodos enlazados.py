# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
	
	# Metodo para vaciar la lista 
	def vacia_lista(self):
		
		num = self.__n
		for i in range(num):
			self.elimina_primero()

	# Metodo para mostrar los elementos de la lista 
	def mostrar_n (self):
		
		nodo = self.__primero
		for i in range (self.__n):
			if (i == self.__pos):
				print "(",nodo.info,")", 
			else: 
				print nodo.info, 
			nodo=nodo.sig
	def mostrar(self):

		nodo = self.__primero
		cont = 0
		while (nodo != None):
			if (cont == self.__pos):
				print "(",nodo.info,")", 
			else: 
				print nodo.info,

			nodo = nodo.sig
			cont = cont + 1


	
	# Metodo para eliminar el primer elemento de la lista
	def eliminar_prim(self):
		
		if (self.__primero == None):
			return
		h = self.__primero
		self.__primero = h.sig
		if (self.__actual == h):

		
			self.__actual = h.sig

			
		if (self.__ultimo == h):
			
			self.__ultimo = h.sig
			
		self.__n = self.__n - 1
		self.__pos = self.__pos - 1
    	
		    
  	# Metodo para consultar la cantidad de elementos de una lista
	def consulta_n(self):
  
		return self.__n 

	def mezclar(self,l):

		l1 = self.__n
		l2 = l.consulta_n()

		i = 0
		j = 0
		c = Lista()

		while (i < l1 and j < l2):

			if (self.return_elem(i) < l.return_elem(j) ):

				c.insertar_ultimo(self.return_elem(i))
				i = i + 1

			else:

				c.insertar_ultimo(l.return_elem(j))
				j = j + 1

		while (i < l1):

			c.insertar_ultimo(self.return_elem(i))
			i = i + 1
		while (j < l2):

			c.insertar_ultimo(l.return_elem(j))
			j = j + 1

		return c.mostrar()

		


	def return_elem(self,pos):

		nodo = self.__primero
		cont = 0
		while (nodo != None):

			if (cont == pos):

				return nodo.info

			nodo = nodo.sig
			cont = cont + 1








			

	def OrdMerge (self):
   		pf = self.__n - 1
   		a1 = Lista()
   		a2 = Lista()
   		if (pf == 0):
   			return self

   		pm = pf / 2

   		a1[:pm+1].OrdMerge()
   		a2[pm+1:pf+1].OrdMerge()
   		return a1.mezclar(a2)

		



l = Lista()
l.insertar_ultimo(2)
l.insertar_ultimo(4)
l.insertar_ultimo(6)

l1 = Lista()
l1.insertar_ultimo(5)
l1.insertar_ultimo(10)
l1.insertar_ultimo(15)

print l.mezclar(l1)














    		
    		






