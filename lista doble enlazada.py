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
			


	def insertar_inicio2 (self,nodo):
		
		temp = self.__primero
		self.__primero = nodo
		if (self.__actual == nodo):
			self.__actual = self.__primero
			
		if (self.__ultimo == nodo):
			self.__ultimo = self.__ultimo.ant
			self.__ultimo.sig = None
		else:
			temp.sig = self.__primero.sig
		


		nodo.sig = temp
		temp.ant = nodo

		
		

	def insertar_ultimo2(self,nodo):
		
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
	def insertar_actual2 (self,nodo):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
	
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
	def encontrar_mayor(self):


		nodo = self.__primero
		mayor = self.__primero.info
		while (nodo != None):

			if (nodo.sig != None and mayor < nodo.sig.info):


				mayor = nodo.sig.info

			nodo = nodo.sig
		return mayor
	def mover(self,nodo,pos):

		n = self.__primero
		p = 0
		while (n != None):

			if (p == pos):
				if (p == 0):

					self.insertar_inicio2(nodo)
					break

				else:

					if (p == self.__n-1):

						self.insertar_ultimo2(nodo)
						break
					else:

						if (p == self.__pos):

							self.insertar_actual2(nodo)
							break
						else:
							self.insertar2(nodo,p)
							break

			n = n.sig
			p = p + 1
		

	def insertar2(self,nuevo,pos):

		
		aux = self.__primero
		cont = 0

		while (aux != None):

			if (cont == pos):

				j = aux.sig
				aux.sig = nuevo
				nuevo.sig = j
				del j
				return
			aux = aux.sig
			cont = cont + 1



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

	def consecutivos_asc(self):

		nodo = self.__primero

		while (nodo != None):
			siguiente = nodo.sig

			if (siguiente == None):

				return True
			if (nodo.info > siguiente.info):

				return False
			nodo = nodo.sig

	def consecutivos_desc(self):

		nodo = self.__primero

		while (nodo != None):

			siguiente = nodo.sig

			if (siguiente == None):

				return True

			if (nodo.info < siguiente.info):

				return False

			nodo = nodo.sig
	def prob_inter(self):

		nodo = self.__primero
		nodo = nodo.sig.sig.sig.sig.sig
		self.intercambiar(nodo,0)






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

			

			

l = ListaD()


l.insertar_ultimo(0)
l.insertar_ultimo(4)
l.insertar_ultimo(8)
l.insertar_ultimo(3)
l.insertar_ultimo(7)
l.insertar_ultimo(8)
l.insertar_ultimo(50)
l.ordenar()




l.mostrar()









