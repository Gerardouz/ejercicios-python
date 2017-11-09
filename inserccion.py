def ordinserccion(arreglo):
  i = 1
  for elen in arreglo[1:]:
    j = i - 1
    while j >= 0:
      
      if arreglo[j] < elen:
        del arreglo[i]
        arreglo.insert(j+1,elen)
        
        break
      if j == 0 and arreglo[0] >= elen:
        arreglo.remove(elen)
        arreglo.insert(0,elen)
      j = j - 1
    i = i + 1
    
    
  return arreglo
  




arreglo = [5,3,4,2,6,1,7,9,3,8,6]
print arreglo
arreglo = ordinserccion(arreglo)
print arreglo