def OrdBurbuja(arreglo):
    Ordenado = False
    while (Ordenado == False):
        i = 0
        Ordenado = True
        for elem in arreglo[:len(arreglo)-1]:
            if (elem > arreglo[i+1]):
                Ordenado = False
                aux = arreglo[i+1]
                del arreglo[i+1]
                arreglo.insert (i,aux)            
            i = i + 1
    return arreglo

arreglo = [2,4,1,7,5,3,8,9,6]
print arreglo
arreglo = OrdBurbuja(arreglo)
print arreglo