
class Tablero:


				

  def __init__(self):
		self.tablero = [['0','1','0','1','0','1','0','1'],
						['1','0','1','0','1','0','1','0'],
						['0','1','0','1','0','1','0','1'],
						['1','0','1','0','1','0','1','0'],
						['0','1','0','1','0','1','0','1'],
						['1','0','1','0','1','0','1','0'],
						['0','1','0','1','0','1','0','1'],
						['1','0','1','0','1','0','1','0']]	


  def mostrar(self):
     cont = 0
     fila = ('0','1','2','3','4','5','6','7')
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
			

				Tablero.tablero[self.posy][self.posx] = '0'
			else:
				print "Movimiento no valido \n "
				return

		if self.pinta == 1:
			
			if (Tablero.tablero[y][x] == 1 and (y - self.posy == x - self.posx or -(y-self.posy) == x-self.posx or y-self.posy == -(x-self.posx))):

				Tablero.tablero[self.posy][self.posx] = '1'
			else:
				print "Movimiento no valido \n"
				return


		Tablero.tablero[y][x] = "A"

		self.posy = y
		self.posx = x
		
		
			

class Caballo:
    pinta=None
    posy=0
    posx=0
    def __init__(self,p,Tablero):
        self.pinta=p
        if(self.pinta==0):
            self.posx=6
            Tablero.tablero[self.posy][self.posx]="c"
        if(self.pinta==1):
            self.posx=1
            Tablero.tablero[self.posy][self.posx]="C"
    def mover(self,y,x,Tablero):
        if(self.pinta==0):
            if(((self.posy+1==y or self.posy-1==y)and(self.posx+2==x or self.posx-2==x))or((self.posx+1==x or self.posx-1==x) and (self.posy+2==y or self.posy-2==y))):
                if(Tablero.tablero[y][x]==1):
                    self.pinta=1
                Tablero.tablero[self.posy][self.posx]='0'
                Tablero.tablero[y][x]='C'
                self.posy=y
                self.posx=x   
                return
            else:
                print "movimiento no valido"
                return
        if(self.pinta==1):
            if(((self.posy+1==y or self.posy-1==y)and(self.posx+2==x or self.posx-2==x))or((self.posx+1==x or self.posx-1==x) and (self.posy+2==y or self.posy-2==y))):
                if(Tablero.tablero[y][x]==0):
                    self.pinta=0  
                Tablero.tablero[self.posy][self.posx]='1'
                Tablero.tablero[y][x]='C'
                self.posy=y
                self.posx=x
            
            
            else:
                print "movimiento no valido en 1"
                return



class Reina:
    posx = 0
    posy = 0
    pinta = None
    def __init__(self,p,Tablero):
        self.pinta = p
        
        if (self.pinta == 0):
            self.posx = 4
        
        if (self.pinta == 1):
            self.posx = 3
            
        Tablero.tablero[self.posy][self.posx] = 'Q'
        
        

    def mover(self,y,x,Tablero):
    
       if (self.pinta == 0):
       
       
           if (y - self.posy == x - self.posx or -(y-self.posy) == x-self.posx or y-self.posy == -(x-self.posx)or (self.posy != y and self.posx == x) or (self.posx != x and self.posy == y)):
       
       
              Tablero.tablero[self.posy][self.posx] = '0'
           else:
              print "movimiento no valido"
              return
              
       if (self.pinta == 1):
      
          if (y - self.posy == x - self.posx or -(y-self.posy) == x-self.posx or y-self.posy == -(x-self.posx)or (self.posy != y and self.posx == x) or (self.posx != x and self.posy == y)):
          
              Tablero.tablero[self.posy][self.posx] = '1'
              
          else:
          
              print "movimiento no valido"
              return
              
              
       if (Tablero.tablero[y][x] != self.pinta):
            self.pinta = Tablero.tablero[y][x]
            
        
       Tablero.tablero[y][x] = 'Q'
       self.posx = x
       self.posy = y
            
        
            
           
    
    
        
    
    
        
    
    
            
            
            
		






tablero = Tablero()
reina = Reina(1,tablero)
alfil1 = Alfil(1,tablero)
caballo1 = Caballo(1,tablero)
alfil0 = Alfil(0,tablero)
caballo0 = Caballo(0,tablero)
parar = 's'
while (parar == 's' or parar == 'S'):
    tablero.mostrar()
    
    pieza = raw_input("que pieza desea mover? \n")
    
    if (pieza == 'Q' or pieza == 'q'):
        
        y = int(raw_input("a donde desea mover la reina\nEje y: "))
        x = int(raw_input("Eje x: "))
        reina.mover(y,x,tablero)
        
        tablero.mostrar()
        
    else:
    
        if (pieza == 'C' or pieza == 'c'):
        
            p = int(raw_input("cual caballo 0 o 1\n"))
            
            if p == 0:
            
                y = int(raw_input("a donde desea mover el caballo\nEje y: "))
                x = int(raw_input("Eje x: "))
                caballo0.mover(y,x,tablero)
                tablero.mostrar()
            else:
            
                y = int(raw_input("a donde desea mover el caballo\nEje y: "))
                x = int(raw_input("Eje x: "))
                caballo1.mover(y,x,tablero)
                tablero.mostrar()
                
        else:
        
            if (pieza == 'A' or pieza == 'a'):
            
                p = int(raw_input("cual Alfil 0 o 1\n"))
            
                if p == 0:
            
                    y = int(raw_input("a donde desea mover el Alfil\nEje y: "))
                    x = int(raw_input("Eje x: "))
                    alfil0.mover(y,x,tablero)
                    tablero.mostrar()
                else:
            
                    y = int(raw_input("a donde desea mover el Alfil\nEje y: "))
                    x = int(raw_input("Eje x: "))
                    alfil1.mover(y,x,tablero)
                    tablero.mostrar()
            
                
        
        

    parar = raw_input("desea seguir jugando? s/n\n")
    if parar == 'n':
    
        break
        
        


