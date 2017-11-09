
class Tablero:


				

	def __init__(self):
		self.tablero = [[0,1,0,1,0,1,0,1],
						[1,0,1,0,1,0,1,0],
						[0,1,0,1,0,1,0,1],
						[1,0,1,0,1,0,1,0],
						[0,1,0,1,0,1,0,1],
						[1,0,1,0,1,0,1,0],
						[0,1,0,1,0,1,0,1],
						[1,0,1,0,1,0,1,0]]	


	def mostrar(self):
		cont = 0
		fila = (0,1,2,3,4,5,6,7)
		print " ",fila
		print " "
		for i in self.tablero:
			
			print cont , i
			cont = cont + 1
			
			




class Alfil:

	pinta = None
	posy = 0
	posx = 0

	def __init__(self,p,Tablero):

		self.pinta = p

		if (self.pinta == 0):
			
			self.posx = 2
			Tablero.tablero[self.posy][self.posx] = "A"

		if (self.pinta == 1):
			
			self.posx = 5
			Tablero.tablero[self.posy][self.posx] = "A"


	def mover(self,y,x,Tablero):


		if self.pinta == 0:

			if (Tablero.tablero[y][x] == 0 and (y - self.posy == x - self.posx or -(y-self.posy) == x-self.posx or y-self.posy == -(x-self.posx))):
			

				Tablero.tablero[self.posy][self.posx] = 0
			else:
				print "Movimiento no valido \n "
				return

		if self.pinta == 1:
			
			if (Tablero.tablero[y][x] == 1 and (y - self.posy == x - self.posx or -(y-self.posy) == x-self.posx or y-self.posy == -(x-self.posx))):

				Tablero.tablero[self.posy][self.posx] = 1
			else:
				print "Movimiento no valido \n"
				return


		Tablero.tablero[y][x] = "A"

		self.posy = y
		self.posx = x
		
		
			






		






a = Tablero()
b = Alfil(0,a)
c = Alfil(1,a)

a.mostrar()

b.mover(1,1,a)
c.mover(2,3,a)

a.mostrar()