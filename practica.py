class Nodo:
	def __init__(self,valor):
		self.info = valor
		self.hizq = None
		self.hder = None

class arbolb:
	def __init__(self):
		self.__raiz = None
	
	
	def insertar(self,valor,raiz=None):
	
		if(raiz==None):
			if(self.__raiz==None):
				self.__raiz=Nodo(valor)
				return
				
			else:
				raiz = self.__raiz
				
		if (valor < raiz.info):
		
			if(raiz.hizq==None):
				nodo=Nodo(valor)
				raiz.hizq=nodo
				
			else:
				self.insertar(valor,raiz.hizq)
				
		else:
			if(raiz.hder==None):
				nodo=Nodo(valor)
				raiz.hder=nodo
				
			else:
				self.insertar(valor,raiz.hder)

	def preorden(self,raiz=None):
		if(raiz==None):
			if(self.__raiz==None):
				return
			raiz= self.__raiz
		
		print raiz.info
		if(raiz.hizq!=None):
			self.preorden(raiz.hizq)
		if(raiz.hder!=None):
			self.preorden(raiz.hder)

	def inorden(self,raiz=None):
		if(raiz==None):
			if(self.__raiz==None):
				return
			raiz= self.__raiz
		
		
		if(raiz.hizq!=None):
			self.inorden(raiz.hizq)
			
		print raiz.info
                
		if(raiz.hder!=None):
			self.inorden(raiz.hder)


	def postorden(self,raiz=None):
		if(raiz==None):
			if(self.__raiz==None):
				return
			raiz= self.__raiz
		
		
		if(raiz.hizq!=None):
			self.postorden(raiz.hizq)
		if(raiz.hder!=None):
			self.postorden(raiz.hder)
			
		print raiz.info

	# Metodo para retornar el nodo izquierdo o derecho de un arbol binario
	def hermano(self,valor,nodo = None):

		if (nodo == None):

			if (self.__raiz == None):
				return

			raiz = self.__raiz

		else:

			raiz = nodo

		if (valor > raiz.info and raiz.hder != None and raiz.hder.info != valor):

			

			return self.hermano(valor,raiz.hder)
			

		if (raiz.hizq == None):

			return False
		x = "hermano izquierdo"
		return x,raiz.hizq.info

		

		if (raiz.hizq != None and raiz.hizq.info != valor):

			return self.hermano(valor,raiz.hder)
			

		if (raiz.hder == None):
			return False
		x = "hermano derecho"
			
		return x,raiz.hder.info
	# Retorna el numero de hojas de un arbol
	def nro_hojas (self,nodo = None):
		
		
		if (nodo == None):

			if (self.__raiz == None):
				
				return

			raiz = self.__raiz

		else:

			raiz = nodo
		g = 0
		h = 0
		if (raiz.hizq == None and raiz.hder == None):
			return 1



		if (raiz.hizq != None):

			h = self.nro_hojas(raiz.hizq)
		

		if (raiz.hder != None):
			g = self.nro_hojas(raiz.hder)


		return g + h

	#Metodo para retornar el tipo del nodo de un arbol
	def tipo_nodo(self,valor,nodo = None):
		if (nodo == None):

			if (self.__raiz == None):
				
				return

			raiz = self.__raiz

		else:

			raiz = nodo
			if (valor == raiz.info):
				return "Raiz"

		if (raiz.hizq != None):

			if (valor == raiz.hizq.info and raiz.hizq.hizq == None and raiz.hizq.hder == None):

				return "Hoja izquierda"

			if (raiz.hizq.info == valor):
				return "Rama izquierda"
		if (raiz.hder != None):


			if (valor == raiz.hder.info and raiz.hder.hizq == None and raiz.hder.hder == None):
				return "Hoja derecha"

			

			if (raiz.hder.info == valor):
				return "Rama derecha"



		if (valor > raiz.info):

			return self.tipo_nodo(valor,raiz.hder)
		return self.tipo_nodo(valor,raiz.hizq)


		def consecutivos(self,nodo = None):
		g = 0
		h = 0
		
		if (nodo == None):

			if (self.__raiz == None):
				
				return 

			raiz = self.__raiz
			
		

		else:

			raiz = nodo

		if(raiz.hizq!=None):
			g = self.consecutivos(raiz.hizq)
			
		
                
		if(raiz.hder!=None):
			h = self.consecutivos(raiz.hder)
	
		return raiz.info















l = arbolb()

l.insertar(4)
l.insertar(7)
l.insertar(3)
l.insertar(2)
l.insertar(8)
print "hermano: \n"
print l.hermano(3), "\n"
print "tipo del nodo: \n"
print l.tipo_nodo(7), "\n"
print "numero de hojas: \n"
print l.nro_hojas(), "\n"

