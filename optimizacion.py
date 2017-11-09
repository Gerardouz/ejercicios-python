from math import sin



x0 = float(raw_input("x0: "))
x1 = float(raw_input("x1: "))
x2 = float(raw_input("x2: "))


fx0 = 2*sin(x0) - pow(x0,2)/10.0
fx1 = 2*sin(x1) - pow(x1,2)/10.0
fx2 = 2*sin(x2) - pow(x2,2)/10.0

x3 = (fx0*(pow(x1,2)-pow(x2,2)) + fx1*(pow(x2,2)-pow(x0,2)) + fx2*(pow(x0,2)-pow(x1,2))) / (2*fx0*(x1-x2) + 2* fx1*(x2-x0) + 2*fx2*(x0-x1))

fx3 = 2*sin(x3) - pow(x3,2)/10.0

print " x3: ", x3
print "f(x3): ", fx3