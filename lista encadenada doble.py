class NodoD:
	def __init__(self,valor):
		self.info = valor
		self.sig = None
		self.ant = None

class ListaD:
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0

	def insertar_primero (self, valor):
		nodo = NodoD(valor)
		
		nodo.sig = self.__primero
		nodo.ant = None 

		if (nodo.sig != None):
			nodo.sig.ant = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo
		self.__primero = nodo
		
		if (self.__ultimo == None):
			self.__ultimo = nodo
		

	def insertar_ultimo (self, valor):
		nodo = NodoD(valor)	

		nodo.sig = None 
		nodo.ant = self.__ultimo 
		

		if (nodo.ant != None):
			nodo.ant.sig = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo
		self.__ultimo = nodo
		if (self.__primero == None):
			self.__primero = nodo

	def cons_primero(self):
		return self.__primero.info
	def cons_actual(self):
		return self.__actual.info
	def cons_ultimo(self):
		return self.__ultimo.info
		
	def insertar (self, valor):
		if (self.__primero == None):
			self.insertar_primero(valor)
			return

		if (self.__actual == self.__ultimo):
			self.insertar_ultimo(valor)
			return

		nodo = NodoD(valor)
		
		nodo.sig = self.__actual.sig
		nodo.ant = self.__actual
		
		nodo.sig.ant = nodo
		nodo.ant.sig = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo

	def sig (self):
		if (self.__actual != None and self.__actual != self.__ultimo):
			self.__actual = self.__actual.sig

	def ant(self):
		if (self.__actual != None and self.__actual != self.__primero):
			self.__actual = self.__actual.ant
			
	def mostrar(self):
		nodo = self.__primero
		while (nodo != None):
			if (nodo == self.__actual):
				print "(", nodo.info, ")",
			else:
				print nodo.info,
			nodo = nodo.sig
		print
			
	def mostrar_inv(self):
		nodo = self.__ultimo
		while (nodo != None):
			if (nodo == self.__actual):
				print "(", nodo.info, ")",
			else:
				print nodo.info,
			nodo = nodo.ant
	# Metodo para intercambiar los valores de un nodo y el nodo de una posicion dada por parametro
	def intercambiar(self,nodo,pos):

		if (nodo == None):
			return
		if (pos >= self.__n):
			self.intercambiar(nodo,self.__n - 1)
			return
		n = self.__primero
		cont = 0
		while (n != None):

			if (cont == pos):

				h = nodo.info
				nodo.info = n.info
				n.info = h
				del h
				return

			cont = cont + 1
			n = n.sig
	# Metodo para verificar si hay numeros repetidos en la lista

	def numeros_repetidos(self):

		nodo = self.__primero

		cont = 0

		while (nodo != None):

			valor = nodo.sig
			while (valor != None):

				if (nodo.info == valor.info):

					cont = cont + 1

				valor = valor.sig

			nodo = nodo.sig

		if (cont > 0):

			return True

		if (cont == 0):

			return False

	# Metodo para consultar la cantidad de elementos de una lista

	def consulta_n(self):

		return self.__n

	# Metodo para saber si dos listas son iguales

	def listas_iguales(self,lista):


		if (self.__n != lista.consulta_n() ):

			return False

		nodo1 = self.__primero
		nodo2 = lista.__primero
		cont = 0

		while (nodo1 != None and nodo2 != None):

			if (nodo1.info != nodo2.info):
				return False

			nodo1 = nodo1.sig
			nodo2 = nodo2.sig

		return True

	# Metodo para sumar los elementos de una lista multitipo

	def sumar_lista(self):

		suma = 0

		nodo = self.__primero

		while (nodo != None):

			if (type(nodo.info) == int):

				suma = suma + nodo.info

			nodo = nodo.sig

		return suma
	# Metodo para saber si una lista tiene sus elementos consecutivos (ascendiente)
	def consecutivos_asc(self):

		nodo = self.__primero

		while (nodo != None):
			siguiente = nodo.sig

			if (siguiente == None):

				return True
			if (nodo.info > siguiente.info):

				return False
			nodo = nodo.sig

		return True
	#Metodo para saber si una lista tiene sus elementos consecutivos (descendiente)
	def consecutivos_desc(self):

		nodo = self.__primero

		while (nodo != None):

			siguiente = nodo.sig

			if (siguiente == None):

				return True

			if (nodo.info < siguiente.info):

				return False

			nodo = nodo.sig

	#Metodo que retorna el mayor elemento de una lista
	def encontrar_mayor(self):


		nodo = self.__primero
		mayor = self.__primero.info
		while (nodo != None):

			if (nodo.sig != None and mayor < nodo.sig.info):


				mayor = nodo.sig.info

			nodo = nodo.sig
		return mayor
			
	# Metodo para mezclar dos listas ordenadas 
	def mezclar(self,l):

		l1 = self.__n
		l2 = l.consulta_n()

		i = 0
		j = 0
		c = ListaD()

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
	
	#Metodo que retorna el elemento que este en la posicion dada por parametro
	def return_elem(self,pos):

		nodo = self.__primero
		cont = 0
		while (nodo != None):

			if (cont == pos):

				return nodo.info

			nodo = nodo.sig
			cont = cont + 1
			
			
	#Metodo para ordenar la lista a traves del metodo burbuja
	def ordenar(self):

		nodo = self.__primero
		ordenado = False
		cont = 0
		while (ordenado == False):
			


			if (nodo.sig == None):
				nodo = self.__primero
				cont = 0

			
			if (nodo.info > nodo.sig.info):

				self.intercambiar(nodo,cont + 1)
				

			if (self.consecutivos_asc() == True):
				ordenado = True
				return

			

			nodo = nodo.sig
			cont = cont + 1





