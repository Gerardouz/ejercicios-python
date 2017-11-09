arreglo = [[1,1,1,0,0],
           [1,1,0],
           [0,0,1,1],
           [1,0,1,0,1],
           [1,1]]
           
cont1max = 0
maxC = 0
for fila in arreglo:
    if (len(fila) > maxC):
        maxC = len(fila)
        
for nCol in range(0,maxC):
    
    Cont1, Cont0 = 0,0
    for fila in arreglo:
        if (len(fila) > nCol):
            if (fila[nCol] == 1):
                Cont1 = Cont1 + 1
                if Cont1 > cont1max:
                  cont1max = Cont1
                  columna = nCol
                
            else:
                Cont0 = Cont0 + 1
    
    if (Cont1 > Cont0):
        print (nCol)
print "la columna con mas unos es ",columna," y tiene",cont1max,"unos"