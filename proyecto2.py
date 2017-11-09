
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


	def prim2(self, nOrigen, nDestino, inicializador=True):
		if(inicializador):
			self.__listaC = []
			self.__arco_mayor = []
			self.peso_arista = 0
			
				
		self.__listaC.append(nOrigen.info)
		for arco in nOrigen.arcos:
			if(self.existe_camino(arco.nodo.info,nDestino.info)==False):
				continue
			if(arco.peso > self.peso_arista):
				self.peso_arista=arco.peso
				self.__arco_mayor.append(nOrigen.info)
				self.__arco_mayor.append(arco.nodo.info)
			if(arco.nodo.info in self.__listaC):
				continue
				
			self.prim2(arco.nodo,nDestino,False)
		for i in self.__arco_mayor:
			if(len(self.__arco_mayor)>2):
				del self.__arco_mayor[0]
				del self.__arco_mayor[0]
		
		return self.__arco_mayor,self.peso_arista
				
				
				
	def prim (self,nodo ):

		try:

			self.__camino.append(nodo.info)
			nodo.visto = True
			self.__aristas = self.__aristas + nodo.arcos

			
		except AttributeError:
			self.__camino = [nodo.info]
			self.__pesocamino = 0
			self.__arbol = Arboln()
			self.__arbol.insertar(nodo.info)
			self.__aristas = nodo.arcos
			
		
		peso = -1
		
		for arco in self.__aristas:

			if (arco.nodo.info in self.__camino):
				continue
			
			if(((peso > arco.peso  or  peso < 0) and arco.nodo.visto == False) ):
				peso = arco.peso
				self.__arcomin = arco

			
		if (self.__arbol.buscar(self.__arcomin.nodo.info) == False):
			self.__arbol.insertar(self.__arcomin.nodo.info,nodo.info)
			self.__pesocamino = self.__pesocamino + self.__arcomin.peso
			
		
		if(self.__arcomin.nodo.visto==True):
			return True

		if (self.prim(self.__arcomin.nodo)):
			return self.__pesocamino,self.__arbol, self.__camino
		return self.__pesocamino,self.__arbol, self.__camino

		



		






					
# Principal

g = Grafo(dirigido = False)
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")
nodo5 = g.ins_nodo("E")
nodo6 = g.ins_nodo("F")
nodo7 = g.ins_nodo("G")


nodo1.enlace(nodo2,7,True)
nodo1.enlace(nodo4,15,True)
nodo2.enlace(nodo3,8,True)
nodo2.enlace(nodo4,9,True)
nodo2.enlace(nodo5,7,True)
nodo5.enlace(nodo3,5,True)
nodo5.enlace(nodo6,8,True)
nodo5.enlace(nodo4,15,True)

nodo4.enlace(nodo6,6,True)
nodo6.enlace(nodo7,11,True)
nodo7.enlace(nodo5,9,True)
#la salida para este grafo debe ser peso de 39 comenzando desde D (nodo4)





peso,arbol,camino = g.prim(nodo4)
print peso
print camino
arbol.preorden()


"""
h = Grafo(dirigido = False)

nodo1 = ins_nodo("A")
nodo2 = ins_nodo("B")
nodo3 = ins_nodo("C")
nodo4 = ins_nodo("D")
nodo5 = ins_nodo("E")
nodo6 = ins_nodo("F")
nodo7 = ins_nodo("G")
nodo8 = ins_nodo("H")

nodo1.enlace(nodo2,1,True)
nodo
"""
