
# Grafo - nodos enlazados -
# Autor: Javier Rivera
from Arboln import Arboln
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.arcos = []
		self.visto = False
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


	def profundidad (self, nodo):
		

		
		try:
			self.__camino.append(nodo.info)
			
			for arco in nodo.arcos:
				if (self.__arbol.buscar(arco.nodo.info) == False and arco.nodo.visto == False):
					self.__arbol.insertar(arco.nodo.info,nodo.info)
					nodo.visto = True
			
		except AttributeError:

			nodo.visto = True
			self.__arbol = Arboln()
			self.__arbol.insertar(nodo.info)
			
			for arco in nodo.arcos:
				self.__arbol.insertar(arco.nodo.info,nodo.info)

			self.__camino = [nodo.info]
			

			
		
		for nodos in self.__nodos:


			if (nodos.info in self.__camino):
				continue
		

				
			self.profundidad(nodos)

		return self.__arbol


	def prim2(self, nodo):

		try:
			
			self.__camino.append(nodo.info)

			for arco in nodo.arcos:
				peso=arco.peso
				if (arco.peso <= peso):
					self.__pesomin = arco.peso

					self.__arcomin = arco

				if (arco.nodo.info in self.__camino):
					continue

			if (self.__arcomin.nodo.visto == False):
				self.__arcomin.nodo.visto = True
				self.prim(self.__arcomin.nodo)
					

		except AttributeError:
			nodo.visto = True
			self.__arbol = Arboln()
			self.__arbol.insertar(nodo.info)
			self.__camino = [nodo.info]
			self.__pesomin = nodo.arcos[0].peso
			self.__arcomin = None

			for arco in nodo.arcos:
				if (arco.peso <= self.__pesomin):
					self.__pesomin = arco.peso
					self.__arcomin = arco
				if (arco.nodo.info in self.__camino):
					continue
			if (self.__arcomin.nodo.visto == False):

				self.prim(self.__arcomin.nodo)


		return self.__camino
		

		
	def prim (self,nodo ):

		try:

			self.__camino.append(nodo.info)

		except AttributeError:
			self.__camino = [nodo.info]
			self.__pesocamino = 0




		for nodos in self.__nodos:
			peso = -1
			nodos.visto=True
			if (nodos.info in self.__camino):
				continue

			for arco in nodos.arcos:
				
				if(peso > arco.peso  or  peso < 0 ):
					peso = arco.peso
					self.__arcomin = arco


			self.prim(nodos)

		return self.__camino

		



		






					
# Principal

g = Grafo()
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")
nodo5 = g.ins_nodo("E")
nodo6 = g.ins_nodo("F")
nodo7 = g.ins_nodo("G")
nodo8 = g.ins_nodo("H")



nodo1.enlace(nodo2,7)
nodo2.enlace(nodo3,10)
nodo3.enlace(nodo1,14)
nodo2.enlace(nodo4,2)
nodo3.enlace(nodo4,3)
nodo4.enlace(nodo5)
nodo4.enlace(nodo6,9)
nodo6.enlace(nodo7,6)
nodo2.enlace(nodo8,10)



#g.profundidad(nodo2).preorden()
print g.prim(nodo1)