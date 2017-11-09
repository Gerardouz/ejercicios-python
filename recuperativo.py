'''COLABORADORES:
MARIA COLMENARES CI: 25033192
GERARDO UZCATEGUI CI:23391131
ORLANDO ORTEGA CI: 24552700
'''
#CLASE NODO DE ARBOL BINARIO
class Nodob:
	def __init__ (self, valor):
		self.info = valor
		self.hizq = None
		self.hder = None
#CLASE DE ARBOL BINARIO
class Arbolb:
	def __init__(self):
		self.__raiz = None

	#METODO PARA INSERTAR VALORES EN UN ARBOL
	def insertar(self, valor, raiz = None):
	
		if (raiz == None):
			if (self.__raiz == None):
				self.__raiz = Nodob(valor)
				return
			raiz = self.__raiz
				
		if (valor < raiz.info):
			if(raiz.hizq == None):
				raiz.hizq = Nodob(valor)
			else:
				self.insertar (valor, raiz.hizq)
		else:
			if (raiz.hder == None):
				raiz.hder = Nodob(valor)
			else:
				self.insertar (valor, raiz.hder)
	#METODO DE PREORDEN DE UN ARBOL BINARIO
	def preorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
		
		print raiz.info,
		if (raiz.hizq != None):
			self.preorden (raiz.hizq)
		if (raiz.hder != None):
			self.preorden (raiz.hder)
	
	#METODO DE POSTORDEN EN UN ARBOL BINARIO
	def postorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.postorden (raiz.hizq)
		if (raiz.hder != None):
			self.postorden (raiz.hder)
		print raiz.info,	

	#METODO DE INORDEN EN UN ARBOL BINARIO
	def inorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.inorden (raiz.hizq)
		print raiz.info,
		if (raiz.hder != None):
			self.inorden (raiz.hder)


	#METODO QUE RETORNA SI EL ARBOL NO ES CONSECUTIVO INDICA LOS VALORES QUE HACEN FALTA
	def faltantes (self, raiz = None):
		if (raiz == None):
			self.__faltantes = []
			
			if (self.__raiz == None):
				return False
			raiz = self.__raiz

		self.__mayor = self.__menor =  raiz.info

		if (raiz.hizq != None):

			M = self.__mayor
			self.faltantes(raiz.hizq)

			if (self.__mayor + 1 != raiz.info):

				for i in range(self.__mayor,raiz.info-1):
					self.__faltantes.append(i+1)

			self.__mayor = M

		if (raiz.hder != None):

			m = self.__menor
			self.faltantes(raiz.hder)

			if (self.__menor - 1 != raiz.info):

				for i in range(self.__menor,raiz.info+1,-1):

					self.__faltantes.insert(0,i-1)

			self.__menor = m

		if (len(self.__faltantes) > 0):
			return self.__faltantes
		return False


	#METODO QUE INDICA SI EL ARBOL ES PERFECTO
	def perfecto(self, raiz = None,n = 0):

		if (raiz == None):

			if (self.__raiz == None or (self.__raiz.hizq == None and self.__raiz.hder == None) ):

				return True
			raiz = self.__raiz

		if (raiz.hizq == None and raiz.hder == None):
			
			return n
		h,g = 0,0
		if (raiz.hizq != None):

			g = self.perfecto(raiz.hizq,n + 1)

		if (raiz.hder != None):

			h = self.perfecto(raiz.hder,n + 1 )
		
		if (type(g) == type (h) and g == h):
			return True
		return False



#PRINCIPAL


print ("CASOS DE PRUEBA:\n")
####################################################################################

print ("caso 1: arbol vacio \n")

a = Arbolb()
#si el arbol es vacio retorna False porque no necesita elementos para ser consecutivo
print ("metodo de faltantes:\n")
print a.faltantes()

#si el arbol es vacio el metodo perfecto retorna True pues se considera un arbol perfecto
print ("metodo de arbol perfecto:\n")
print a.perfecto()

######################################################################################


print ("caso 2: arbol con solo la raiz \n")
b = Arbolb()

b.insertar(6)
# si no hacen falta elementos para ser consecutivo retorna False
print ("metodo de faltantes:\n")
print b.faltantes()
# si el arbol solo cuenta con la raiz retorna True porque cumple con las condiciones para ser perfecto
print ("metodo de perfecto: \n")
print b.perfecto()

########################################################################################


print ("caso 3: arbol con la raiz y dos hijos \n")
c = Arbolb()
#insertar elemento
c.insertar(9)
c.insertar(4)
c.insertar(10)
#retorna los numeros faltantes para ser consecutivo
c.preorden()
print ("\n")
print ("metodo de faltantes:\n")
print c.faltantes()
#retorna True porque el arbol es perfecto
print ("metodo de perfecto: \n")
print c.perfecto()

#########################################################################################

#arbol de 2 niveles
print ("caso 4: arbol de dos niveles  \n")
d = Arbolb()
#insertar elemento
d.insertar(6)
d.insertar(4)
d.insertar(9)
d.insertar(2)
d.insertar(5)
d.insertar(7)
d.insertar(10)
d.preorden()
print ("\n")
#muestra los numeros faltantes para ser consecutivo
print ("metodo de faltantes:\n")
print d.faltantes()
# retorna True por ser el arbol perfecto
print ("metodo de perfecto: \n")
print d.perfecto()

###########################################################################################


############################################################################################
print ("caso 5 arbol no perfecto \n")

e = Arbolb()

e.insertar(10)
e.insertar(6)
e.insertar(5)
e.insertar(7)
e.insertar(11)
e.preorden()
print ("\n")
#retorna False ya que el arbol no es perfecto
print ("metodo de arbol perfecto:\n")
print e.perfecto()

############################################################################################

