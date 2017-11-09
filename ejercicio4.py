a = [4,8,9,7,5,9]
b = [4,9,9,7,5,8]
x = 0
y = 0
for i in a:
  if i == b[x]:
    y = y + 1
  x = x +1
if y == len(a):
  print "tienen el mismo orden"
else:
  print "no tienen el mismo orden"