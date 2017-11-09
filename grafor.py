# Grafo - nodos enlazados -
# Autor: Javier Rivera

class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.arcos = []
		
	def enlace (self, ndestino, peso = 1, bdir = False):
		if (type(ndestino) == type(self)):
			arco = Arco(ndestino, peso)
			self.arcos.append(arco)
			if (bdir == True):
				arco = Arco(self, peso)
				ndestino.arcos.append(arco)
			return True
		return False
		
	def muestra_enlaces (self):
		for arco in self.arcos: 
			print arco.nodo.info,
			print arco.peso
			
	def existe_enlace(self, ndestino):
		for arco in self.arcos:
			if (arco.nodo == ndestino):
				return arco
		return False
	def existe_enlace_peso(self, ndestino):
		for arco in self.arcos:
			if (arco.nodo == ndestino):
				return arco
		return False
		
	def eli_enlace (self, ndestino):
		arco = self.existe_enlace(ndestino)
		if (arco != False):
			self.arcos.remove(arco)
			return True
		return False
			
	def __del__(self):
		del self.arcos
		
class Arco:
	def __init__ (self, ndestino, peso=0):
		self.nodo = ndestino
		self.peso = peso

class Grafo:
	def __init__(self, dirigido = True):
		self.__nodos = []
		self.__dirigido = dirigido
		
	def buscaNodo (self, valor):
		for nodo in self.__nodos:
			if (nodo.info == valor):
				return nodo
		return False
	
	def enlace(self, valOrigen, valDestino, peso = 1, bdir = False):
		
		norigen = self.buscaNodo(valOrigen)
		if (not(norigen)):
			return False
			
		ndestino = self.buscaNodo(valDestino)
		if (not(ndestino)):
			return False
		
		if (self.__dirigido == False):
			bdir = True
			
		norigen.enlace(ndestino, peso, bdir)
		return True
		
	def ins_nodo (self, valor):
		if (self.buscaNodo(valor) == False):
			nodo = Nodo(valor)
			self.__nodos.append(nodo)
			return nodo
		return False
		
	def eli_nodo(self, valor):
		nodoE = self.buscaNodo(valor)
		if (nodoE == False):
			return False
			
		for nodo in self.__nodos:
			nodo.eli_enlace(nodoE)
		
		self.__nodos.remove(nodoE)
		return True
	
	def existen_islas(self):
		for nodo in self.__nodos:
			if (len(nodo.arcos) == 0):
				esIsla = True
				for norigen in self.__nodos:
					if (norigen.existe_enlace(nodo) != False):
						esIsla = False
						break
						
				if (esIsla == True):
					return True
		return False
		
	def __str__(self):
		grafo  = ""
		for nodo in self.__nodos:
			grafo = grafo + nodo.info
			arcos = ""
			for arco in nodo.arcos:
				if (arcos != ""):
					arcos = arcos + ", "
				arcos = arcos + arco.nodo.info + ":" + str(arco.peso)
			grafo = grafo + "(" + arcos + ") "
		return grafo

	def existe_camino2(self, nOrigen, nDestino, inicializador=True):
			if (inicializador == True):
				self.__listaC=[]
			self.__listaC.append(nOrigen.info)
			if (nOrigen.existe_enlace(nDestino)):
				self.__listaC.append(nDestino.info)
				return True,self.__listaC

			for arco in nOrigen.arcos:
				if (arco.nodo.info in self.__listaC):
					continue
				encuentra = self.existe_camino(arco.nodo, nDestino,False)

				if (encuentra):
					return True
				self.__listaC.pop(len(self.__listaC)-1)

			return False

	#indica que nodo tiene mas aristas de salidas 
	def nodoMasSalidas(self):
		mayor = 0
		for nodo in self.__nodos:
			if (len(nodo.arcos) > mayor):
				mayor=len(nodo.arcos)
				vertice=nodo.info
			
		return vertice , mayor
			
	#indica que nodo tiene mas aristas de llegada
	def nodoMasllegadas(self):
		mayor = 0
		for nodo in self.__nodos:
			con=self.entradas(nodo.info) 
			if (con > mayor ):			
				mayor = con
				vertice = nodo.info

		return vertice , mayor
						 
	def entradas (self, valor):
		cont = 0
		for nodo in self.__nodos :
			for arco in nodo.arcos :
				if ( arco.nodo.info == valor):
					cont = cont +1
		return cont	
	#indica el nodo con mas lazos
	def nodoMaslaz0s(self):
		cont=0
		mayor=0
		for nodo in self.__nodos:
			for arcos in nodo.arcos:
				if (arcos.nodo.info==nodo.info):
					cont=cont+1
			if(cont>mayor):
				mayor=cont
				vertice=nodo.info

		return vertice , mayor
	
	#verifica si un nodo tiene camino asi mismo
	def caminoAsimismo(self, nOrigen, nDestino, inicializador = True ):

		if (inicializador == True):
			self.__listaC=[]
		self.__listaC.append(nOrigen.info)
		if (nOrigen.existe_enlace(nDestino)):
			self.__listaC.append(nDestino.info)
			return False

		for arco in nOrigen.arcos:
			if (arco.nodo.info in self.__listaC):

				return True

			encuentra = self.existe_camino(arco.nodo, nDestino,False)

			if (encuentra):
				return True,self.__listaC
			self.__listaC.pop(len(self.__listaC)-1)
			self.__eli_enlace(self.__,nDestino)

		return False

	#indica si un grafo es simple
	def Grafosimple(self):
		for nodo in self.__nodos:
			pos = 1
			n=len(nodo.arcos)
			for arco in nodo.arcos:
				if (nodo.info == arco.nodo.info):
					return False

				for arc in range ( pos , n ):
					if (arco.nodo.info == nodo.arcos[arc].nodo.info):
						return False				
				pos = pos + 1
		return True

	#busca el nodo con mas aristas
	def nodoMasAristas(self):
		mayor = 0
		for nodo in self.__nodos:
			salida = len (nodo.arcos)
			entrar = self.entradas(nodo.info)
			suma = salida + entrar

			if(suma > mayor):
				mayor = suma
				vertice = nodo.info
		return mayor , vertice


	def Nodo_que_me_sigue(self, valor):
		lista_seguidores = []

		for nodo in self.__nodos:
			
			for arco in nodo.arcos: 
				
				if(arco.nodo.info == valor ):
					lista_seguidores.append(nodo.info)
		return lista_seguidores

	def Nodo_que_sigo(self, valor):
		b=[]
		for nodo in self.__nodos:
			for arco in nodo.arcos: 
				if(nodo.info == valor): 
					a = self.Nodo_que_me_sigue(valor)
		
					if(arco.nodo.info in  a ):
						b.append(arco.nodo.info)
		return "seguidores",a,"seguidos",b

	#retorna en numeros la cantidad de caminos que exiten entre dos nodos
	def CaminosaDosnodos(self, nOrigen , nDestino, inicializador=True):
		cont=0
		if (inicializador == True):
			self.__listaC=[]
		self.__listaC.append(nOrigen.info)
		if (nOrigen.existe_enlace(nDestino)):
			self.__listaC.append(nDestino.info)
			cont= cont+1

		for arco in nOrigen.arcos:
			if (arco.nodo.info in self.__listaC):
				continue
			encuentra = self.CaminosaDosnodos(arco.nodo, nDestino,False)
			if (encuentra):
				cont=cont+1
			self.__listaC.pop(len(self.__listaC)-1)
			
		return cont
	#el peso que hay de un nodo a otro
	def peso_de_un_camino(self, nOrigen , nDestino, inicializador=True):		
		
		if (inicializador == True):
			self.__listaC = []
			self.__pesos=0
		self.__listaC.append(nOrigen.info)
		existeArco=nOrigen.existe_enlace(nDestino)
		
		if (existeArco):
			self.__listaC.append(nDestino.info)
			self.__pesos=self.__pesos + existeArco.peso
			return True, self.__pesos,self.__listaC
		for arco in nOrigen.arcos:
			
			if (arco.nodo.info in self.__listaC):
				continue
			self.__pesos = self.__pesos + arco.peso
			encuentra = self.peso_de_un_camino(arco.nodo, nDestino,False)
			
			if (encuentra):				
				return True,self.__pesos,self.__listaC

			self.__listaC.pop(len(self.__listaC)-1)
			self.__pesos = self.__pesos - arco.peso

		return False

	def camino_menorDistancia(self, nOrigen , nDestino):
		menor=0
		inicia=0
		camino = []
		for arco in nOrigen.arcos:
			distancia = self.peso_de_un_camino(arco.nodo,nDestino)	
			if (distancia):
				suma=distancia[1]+arco.peso
				if(inicia == 0):
					menor = suma
					inicia += 1
				if (suma <= menor):
					menor= suma
					camino=distancia[2]
					camino.insert(0,nOrigen.info)
		return menor,camino				
	#mostrar como una matriz
	def Muestraenmatrizdeadyacencia(self):
		pass
	#muestra en matriz de incidencia
	def Muestraenmatrizincidencia	(self):
		pass
	#indica si dos grafo son isomorfos
	def grafosIsomorfos(self):
		pass
	#a nivel de nodo decir si un grafo es dirigino o no
	def grafo_dirigidoNodo(self):
		pass
	#convertir un grafo de dirigino a no dirigido
	def convierte_grafo(self):
		pass	
	#cuantos subgrafos exiten 
	def subgrafosEX(self):
		pass
	
	
	def arista_mayor_peso(self, nOrigen , nDestino, inicializador=True):		
		
		if (inicializador == True):
			self.__listaC = []
			self.__otra_lista=[]
			self.__pesos=0
			self.__n = False
		self.__listaC.append(nOrigen.info)
		existeArco=nOrigen.existe_enlace(nDestino)
		
		if (existeArco):
			self.__listaC.append(nDestino.info)
			if ( existeArco.peso > self.__pesos):
			  if (len(self.__otra_lista) != 0):
			    i=0
			    while(i<2):
			      del self.__otra_lista[0]
			      i+=1
			  self.__otra_lista.append(nOrigen.info)
			  self.__otra_lista.append(nDestino.info)
			  self.__pesos=existeArco.peso
			return self.__pesos,self.__otra_lista
		for arco in nOrigen.arcos:
			
			if (arco.nodo.info in self.__listaC):
				continue
			if ( arco.peso > self.__pesos):
			  if (len(self.__otra_lista) != 0):
			    i=0
			    while(i<2):
			      del self.__otra_lista[0]
			      i+=1
			  self.__pesos=arco.peso
			  self.__otra_lista.append(nOrigen.info)
			  self.__otra_lista.append(arco.nodo.info)
			
			encuentra = self.arista_mayor_peso(arco.nodo, nDestino,False)
			
			if (encuentra):				
				return self.__pesos,self.__otra_lista

			self.__listaC.pop(len(self.__listaC)-1)

		return False


	def arista_mayor_peso2(self,norigen,ndestino):

		try:

			self.__camino.append(norigen.info)
			

		except AttributeError:

			self.__camino = [norigen.info]
			self.__arista = []
			self.__peso = 0
			self.__encontro_camino = False
		Arco = norigen.existe_enlace(ndestino)

		if (Arco != False):

			self.__camino.append(ndestino.info)
			
			if (Arco.peso > self.__peso):

				if (len(self.__arista) != 0):

					del self.__arista[:]

				self.__peso = Arco.peso
				self.__arista.append(norigen.info)
				self.__arista.append(ndestino.info)
				self.__encontro_camino = True
			return self.__peso, self.__arista,self.__encontro_camino

		for arco in norigen.arcos:

			if(arco.nodo.info in self.__camino):

				continue

			if (arco.peso > self.__peso):

				if (len(self.__arista) != 0):

					del self.__arista[:]

				
				self.__peso = arco.peso
				self.__arista.append(norigen.info)
				self.__arista.append(arco.nodo.info)

			peso,lista,encontro_camino = self.arista_mayor_peso2(arco.nodo,ndestino)

			if (encontro_camino == False or encontro_camino == None):
				continue

				

		return False, None, None
	def existe_camino(self, valorigen , valdestino ):
		if (self.buscaNodo(valorigen) == False or self.buscaNodo(valdestino) == False):
			return False
		norigen = self.buscaNodo(valorigen)
		ndestino = self.buscaNodo(valdestino)

		try:
			self.__camino.append(norigen.info)
		except:
			self.__camino = [norigen.info]

		if (norigen.existe_enlace(ndestino) != False):
			return True

		for nodo in self.__nodos:

			if (nodo.info in self.__camino):
				continue

			if (self.existe_camino(nodo.info,valdestino)):
				return True, self.__camino
		return False


	def arista_mayor_peso(self,norigen,ndestino):

		try:
			self.__camino.append(norigen.info)

		except AttributeError:
			self.__camino = [norigen.info]
			self.__peso = 0
			self.__nodo1 = norigen.info
			self.__nodo2 = ndestino.info


		for arco in norigen.arcos:
			if(arco.nodo.info in self.__camino):

				continue

			if (arco.peso > self.__peso):
				self.__peso = arco.peso
				self.__nodo1 = norigen.info
				self.__nodo2 = arco.nodo.info

			if (norigen.existe_enlace(ndestino) and arco.nodo == ndestino):
				return self.__nodo1,self.__nodo2,self.__peso

			nodo1,nodo2,peso = self.arista_mayor_peso(arco.nodo,ndestino)

			if (nodo1 == False):
			
				self.__peso = arco.peso
				self.__nodo1 = norigen.info
				self.__nodo2 = arco.nodo.info
				continue
			return self.__nodo1,self.__nodo2,self.__peso

		return False,None,None










		
		
		

				
					
					
				
# Principal

g = Grafo()
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")
nodo5 = g.ins_nodo("E")
nodo6 = g.ins_nodo("F")


#prueba grafo
'''nodo1.enlace(nodo3,1)
nodo1.enlace(nodo1,1)
nodo1.enlace(nodo4,1)
nodo3.enlace(nodo2,1)
nodo3.enlace(nodo4,1)
nodo3.enlace(nodo3,1)
nodo5.enlace(nodo3,1)
nodo1.enlace(nodo2,1)
nodo4.enlace(nodo5,1)
nodo5.enlace(nodo6,1)'''

#prueba2 grafo
nodo1.enlace(nodo2)
nodo2.enlace(nodo3,5)
nodo3.enlace(nodo4,6)
nodo1.enlace(nodo5,3)
nodo5.enlace(nodo6,2)

#print g.peso_de_un_camino(nodo3,nodo6)
#prueba3 grafo
'''nodo1.enlace(nodo1,1)
nodo1.enlace(nodo2,1)
nodo1.enlace(nodo3,1)
nodo2.enlace(nodo3,1)
nodo2.enlace(nodo1,1)
nodo3.enlace(nodo5,1)'''

print g.arista_mayor_peso3(nodo1,nodo6)
# prantica n

'''nodo1.enlace(nodo1,1)
nodo1.enlace(nodo2,1)
nodo1.enlace(nodo3,2)
nodo1.enlace(nodo5,1)
nodo2.enlace(nodo3,1)
nodo2.enlace(nodo5,1)
nodo2.enlace(nodo1,2)
nodo3.enlace(nodo1,1)
nodo4.enlace(nodo2,1)
nodo4.enlace(nodo1,1)
nodo4.enlace(nodo5,1)
nodo5.enlace(nodo4,4)'''



#print g.Nodo_que_me_sigue ("A")

#print g.Grafosimple()
'''
print"nodo mas llegada"
print g.nodoMasllegadas()
print "nodo mas salidas"
print g. nodoMasSalidas()
print"existe camino"
print g.existe_camino(nodo4,nodo6)
print "exise camino asi mismo"
print g.caminoAsimismo(nodo1,nodo1)
'''
'''print " GRAFO "
print g 

print "Enlaces de A"
nodo1.muestra_enlaces()
print "Enlaces de B"
nodo2.muestra_enlaces()

####### xxx #######

g2 = Grafo(False)
				
g2.ins_nodo("A")
g2.ins_nodo("B")
g2.ins_nodo("C")
g2.ins_nodo("D")
g2.ins_nodo("E")

g2.enlace("A","B",2)
g2.enlace("A","C",1)
g2.enlace("B","D",1)
g2.enlace("D","E",1)

print		
print " GRAFO 2"

print g2
		
print "Enlaces de A"
nodoA = g2.buscaNodo("A")
nodoA.muestra_enlaces()

print "Enlaces de B"
nodoB = g2.buscaNodo("B")
nodoB.muestra_enlaces()
		
print "Islas..", g2.existen_islas()

g2.eli_nodo("D")	

print "Islas..", g2.existen_islas()

print g2'''

