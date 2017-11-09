xl = float(raw_input("xl: "))
xu = float(raw_input("xu: "))

R = 0.61803
d = R*(xu - xl)
x1 = xl + d
x2 = xu - d



if (x1 <= 2 or x2 <= 2):
	fl = 3*xl
	F1 = 3*x1
	F2 = 3*x2
	fu = 3*xu
else:
	fl = (-xl + 20)/3.0
	F1 = (-x1 + 20)/3.0
	F2 = (-x2 + 20)/3.0
	fu = (-xu + 20)/3.0
print "xl: ", xl
print "fl: ", fl
print "x1: ", x1
print "f1: ", F1
print "x2: ", x2
print "f2: ", F2
print "xu: ", xu
print "fu: ", fu
print "d: ", d




