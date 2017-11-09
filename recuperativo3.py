arreglo = [5,6,8,11,13,14,17]
x = 0
faltantes = 0
anterior = arreglo[0]
for valor in arreglo:
    if (valor - anterior > 1):
        for n in range(anterior+1,valor):
          x = x + 1
          
          print (n)
        if (x > faltantes):
          faltantes = x
          rango1 = anterior+1
          rango2 = valor-1
    x = 0
    anterior = valor
print ("la secuencia faltante mas grande es entre el",rango1,"y el",rango2,"y es de",faltantes,"elementos")