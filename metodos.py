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


    #metodo que indica si un elemento se encuentra en la lista
    def verificar_elem(self,valor):

        if (self.inicio == None):
            return False

        if (self.inicio.info == valor):
            return True

        nodo = self.inicio.sig

        while (nodo != None):

            if (nodo.info == valor):

                return True
            nodo = nodo.sig

        return False

    #metodo que indica si existen elementos repetidos en la lista
    def existen_repetidos(self):

        nodo = self.inicio

        contador = 0

        while (nodo != None):

            nodo2 = nodo.sig
            while (nodo1 != None):

                if (nodo.info == nodo2.info):

                    cont = cont + 1

                nodo2 = nodo2.sig

            nodo = nodo.sig

        if (contador > 0):

            return True

        return False