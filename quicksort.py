# Metodo de Ordenamiento por Selección 
# pivote a la izquierda



def OrdQuickSort(arreglo):
    
    if (len(arreglo) <= 1):
        return arreglo
    
    i = len(arreglo) - 1
    pivote = 0
    
    while (i > pivote):
        
        if (arreglo[i] < arreglo[pivote]):
            elem = arreglo[i]
            del arreglo[i]
            arreglo.insert(pivote,elem)
            pivote = pivote + 1 
            
        else:
            i = i - 1
    a1 = OrdQuickSort(arreglo[0:pivote])
    a2 = OrdQuickSort(arreglo[pivote+1:])
    
    return a1 + [arreglo[pivote]] + a2

# PRINCIPAL

arreglo = [4,6,2,8,3,5,1,7,9,5]
print arreglo
arreglo = OrdQuickSort(arreglo)        
print arreglo