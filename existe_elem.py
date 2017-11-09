class Nodo:
    def __init__(self,valor):
        self.info = valor
        self.sig = None

class Listas:
    def __init__(self):
        self.inicio = None
        self. n = 0
        
    def agregar_elemento(self, valor):
        nodo = Nodo(valor)
        nodo.sig = self.inicio
        self.inicio = nodo
        self.n = self.n + 1
        
    def mostrar(self):
        nodo = self.inicio
        while (nodo != None):
            print (nodo.info)
            nodo = nodo.sig
        
    def elimina_primero(self):
        nodo = self.inicio
        self.inicio = nodo.sig
        del nodo
        self.n = self.n - 1
        
    def num(self):
        return self.n 
        
    def elemento_posicion(self, pos):
        i = 0
        nodo = self.inicio
        while (nodo != None):
            if (pos == i): 
                return nodo.info
            i = i + 1
            nodo = nodo.sig
            
    def agregar_elemento_pos(self, valor, pos):
        i = 0
        nodo = self.inicio
        while (nodo != None):
            if (pos-1 == i): 
                break
            i = i + 1
            nodo = nodo.sig
            
        nuevo = Nodo(valor)
        nuevo.sig = nodo.sig
        nodo.sig = nuevo




#Programa que indica si un elemento se encuentra en la lista
valor = int(input("ingrese el numero que desea verificar en la lista "))

lista = Listas()

lista.agregar_elemento(4)
lista.agregar_elemento(20)
lista.agregar_elemento(9)

nodo = a.inicio
existe = False

if (nodo == None):
    print (False)
    
else:
    while (nodo != None):

        if (nodo.info == valor):

            print (True)
            existe = True
            break
        nodo = nodo.sig

if (existe != True):
    print (False)