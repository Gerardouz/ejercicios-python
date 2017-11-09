a = [8,6,5,9,9,8,8,9,0,0,0]
n = []
y = 0
for i in a:
  x = 0
  for j in a:
    if i == j:
      x = x + 1
  if x >= y:
    y = x
    u = i in n
    if u == False:
        n.append(i)
    if u == True:
        n.remove(i)
print ("los elementos que se repiten son " , n , "y se repiten ", y ,"veces")